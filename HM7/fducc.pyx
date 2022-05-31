import networkx as nx

cdef class Data:

    cdef list _catagories, _items
    cdef dict _agents_evaluation

    def __init__(self,catagories, a_evaluation,items):
        self._catagories = catagories
        self._items = items
        self._agents_evaluation = a_evaluation

cpdef dict ef1_algorithm(agents_names, f):
    cdef dict allocation ={a:{k:set() for k in f._catagories} for a in agents_names}
    cdef list sigma = [a for a in agents_names]
    for category in f._catagories:
        envy_graph = nx.DiGraph()
        Bh = greedy_round_robin(category ,f._items, sigma , f._agents_evaluation)
        {key:allocation[key][category].update(Bh[key]) for key in allocation.keys()}
        for agent in agents_names:
            envy_graph.add_node( agent ,bundel = allocation[agent])
        sigma = lemma_1(envy_graph, f._agents_evaluation, allocation, category, sigma)
        if sigma == None:
            return None
    return allocation

cdef dict greedy_round_robin(category, items, agents, agents_evaluation):
    cdef int index =0
    cdef dict allocation = {a:set() for a in agents}
    cdef set M =  {k for k in agents_evaluation[agents[index]][category].keys()}
    while len(M) != 0:
        for i in range(len(set(M))):
            agent_name = agents[index % len(agents)]
            evaluation_arr = dict({key:value for key, value in agents_evaluation[agent_name][category].items() if key in M})
            max_item = max(evaluation_arr, key =lambda x: evaluation_arr[x])
            allocation[agent_name].add(max_item)
            M.discard(max_item)
            index += 1
    return allocation


cdef list lemma_1(envy_graph, evaluation, allocation, category, sigma):
    generate_envy(envy_graph, evaluation, category, allocation)
    if (list(nx.simple_cycles(envy_graph))):
        cycles = list(nx.simple_cycles(envy_graph))
        for loop in cycles:
            for node in loop:
                rest_of_nodes = set(sigma).difference(set(loop))
                for other in rest_of_nodes:
                    if not envy_graph.has_edge(node, other):
                        current_g = nx.DiGraph(envy_graph)
                        current_a = allocation
                        change_allocation(envy_graph, node, other, evaluation, allocation, category)
                        if(list(nx.simple_cycles(envy_graph))):
                            envy_graph = current_g
                            allocation = current_a
                        else:
                            return list(nx.topological_sort(envy_graph))
            else:
                return None
        sigma = lemma_1(envy_graph, evaluation, allocation, category, sigma)
    else:   
        return sigma

cdef generate_envy(envy_graph, evaluation, category, allocation):
    envy_graph.remove_edges_from(list(envy_graph.edges()))
    for agent_u in allocation.keys():
        for agent_v in allocation.keys():
            if agent_u != agent_v:
                u_eval = sum_values(agent_u, evaluation, category, allocation[agent_u])
                v_eval = sum_values(agent_v, evaluation, category, allocation[agent_u])
                if v_eval > u_eval :
                    envy_graph.add_edge(agent_u, agent_v)

cdef change_allocation(envy_graph, src, dst, evaluation, allocation, category):
    place_holder = allocation[dst][category]
    allocation[dst][category] = allocation[src][category]
    allocation[src][category] = place_holder
    generate_envy(envy_graph, evaluation, category, allocation)

cdef int sum_values(agent_name, evaluation, category, allocations):
    return sum([sum(evaluation[agent_name][category][item] for x in evaluation[agent_name][category] if x == item )for item in allocations[category]])