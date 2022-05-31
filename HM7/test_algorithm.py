import fair_division_under_cardinality_constraints as fair_division_python
import fducc as fair_division_cython
import time 

def plot_time_graph(input_size:list, runntime:list, impoved_runntime:list):
    
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    plt.plot(input_size, runntime)
    plt.plot(input_size,impoved_runntime)
    plt.xlabel('Input Size')
    plt.ylabel('Time Complexity')
    plt.show()


def get_n_size(catagories:list, items:dict, agents_names:list):

    count =0
    for category in catagories:
        temp = items[category]
        for _ in temp:
            count += 1
    return count + len(agents_names) + len(catagories)

def evaluate_improvment_from_original():

    runntime, improved_runntime, n_size, count = [], [], [], 0, 
    
    # example 1 -small size items
    agents_evaluation ={
                "a": {"trees": {"oak":8,"sprouce":9,"sakoia":9,"mango":2},"doors":{"white":8,"black":1,"red":4,"green":5}}, 
                "b":{"trees": {"oak":2,"sprouce":2,"sakoia":2,"mango":2},"doors":{"white":1,"black":4,"red":2,"green":9}}
                }
    catagories  = ["trees", "doors"]
    items = {"trees":{"oak","sprouce","sakoia","mango"},"doors":{"white","black","red","green"}}
    agents_names = ['a','b']

    # python implementation of the algorithm.
    n_size.append(get_n_size(catagories, items, agents_names))
    data = fair_division_python.Data(catagories,agents_evaluation,items)
    start = time.perf_counter()
    allocation = fair_division_python.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    runntime.append(total_time) 

    # cython (C generated python) implementation of the algorithm.
    start = time.perf_counter()
    allocation = fair_division_cython.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    improved_runntime.append(total_time) 
    
    # example 2 - small size agents list
    agents_evaluation ={
                "a": {"trees": {"oak":8,"sprouce":9,"sakoia":9,"mango":2},"doors":{"white":8,"black":1,"red":4,"green":5}}, 
                "b":{"trees": {"oak":2,"sprouce":2,"sakoia":2,"mango":2},"doors":{"white":1,"black":4,"red":2,"green":9}},
                "c":{"trees": {"oak":2,"sprouce":5,"sakoia":8,"mango":7},"doors":{"white":4,"black":6,"red":3,"green":7}
            }}
    catagories  = ["trees", "doors"]
    items = {"trees":{"oak","sprouce","sakoia","mango"},"doors":{"white","black","red","green"}}
    agents_names = ['a','b','c']

    # python implementation of the algorithm.
    n_size.append(get_n_size(catagories, items, agents_names))
    data = fair_division_python.Data(catagories,agents_evaluation,items)
    start = time.perf_counter()
    allocation = fair_division_python.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    runntime.append(total_time) 

    # cython (C generated python) implementation of the algorithm.
    start = time.perf_counter()
    allocation = fair_division_cython.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    improved_runntime.append(total_time) 

    #example 3  - mid size items items
    agents_evaluation ={
        'a': {'laptop': {'red': 2664, 'blue': 7790, 'green': 2135, 'black': 4682, 'white': 7918, 'magenta': 3504, 'big': 5141, 'small': 1709, 'deep': 2244}, 
            'remote control': {'red': 5303, 'blue': 1151, 'green': 8198, 'black': 9745, 'white': 7468, 'magenta': 8893, 'big': 5374, 'small': 5723, 'deep': 9742}, 
            'bowl': {'red': 9581, 'blue': 2479, 'green': 9254, 'black': 1518, 'white': 9553, 'magenta': 8540, 'big': 2044, 'small': 2469, 'deep': 1260}, 
            'spoon': {'red': 9813, 'blue': 4762, 'green': 9068, 'black': 5938, 'white': 2455, 'magenta': 4479, 'big': 4589, 'small': 5615, 'deep': 6783}, 
            'fork': {'red': 9499, 'blue': 9902, 'green': 2346, 'black': 3576, 'white': 5256, 'magenta': 9194, 'big': 5907, 'small': 2480, 'deep': 6050},
            'pot': {'red': 1924, 'blue': 4253, 'green': 2660, 'black': 5044, 'white': 398, 'magenta': 4712, 'big': 566, 'small': 7827, 'deep': 5331}, 
            'keys': {'red': 6377, 'blue': 1817, 'green': 2168, 'black': 7145, 'white': 6174, 'magenta': 1173, 'big': 4727, 'small': 3071, 'deep': 5321}
            },
        'b': 
            {'laptop': {'red': 8711, 'blue': 7057, 'green': 8600, 'black': 1814, 'white': 1594, 'magenta': 5538, 'big': 8264, 'small': 5919, 'deep': 6214}, 
            'remote control': {'red': 7014, 'blue': 9447, 'green': 3588, 'black': 9808, 'white': 8052, 'magenta': 9037, 'big': 4443, 'small': 2781, 'deep': 2401}, 
            'bowl': {'red': 451, 'blue': 9272, 'green': 6137, 'black': 2175, 'white': 8825, 'magenta': 1551, 'big': 3374, 'small': 145, 'deep': 1746},
            'spoon': {'red': 8696, 'blue': 6937, 'green': 5014, 'black': 4811, 'white': 7933, 'magenta': 8789, 'big': 1994, 'small': 8521, 'deep': 6718}, 
            'fork': {'red': 3491, 'blue': 9971, 'green': 1142, 'black': 5207, 'white': 8201, 'magenta': 2103, 'big': 6957, 'small': 6645, 'deep': 4696}, 
            'pot': {'red': 5098, 'blue': 5763, 'green': 465, 'black': 5313, 'white': 9537, 'magenta': 8083, 'big': 5839, 'small': 1410, 'deep': 4229}, 
            'keys': {'red': 7560, 'blue': 8046, 'green': 5437, 'black': 7753, 'white': 6732, 'magenta': 1564, 'big': 7221, 'small': 8994, 'deep': 7902}
            }, 
        'c':
            {'laptop': {'red': 5705, 'blue': 8525, 'green': 9884, 'black': 9246, 'white': 9797, 'magenta': 8899, 'big': 9138, 'small': 6625, 'deep': 6688}, 
            'remote control': {'red': 140, 'blue': 8156, 'green': 679, 'black': 665, 'white': 4650, 'magenta': 4993, 'big': 3659, 'small': 1030, 'deep': 846}, 
            'bowl': {'red': 2001, 'blue': 1315, 'green': 7379, 'black': 1803, 'white': 3521, 'magenta': 809, 'big': 839, 'small': 4819, 'deep': 5361}, 
            'spoon': {'red': 3040, 'blue': 5005, 'green': 2352, 'black': 4177, 'white': 7848, 'magenta': 7627, 'big': 5748, 'small': 6219, 'deep': 1152}, 
            'fork': {'red': 2369, 'blue': 648, 'green': 6321, 'black': 1728, 'white': 6628, 'magenta': 522, 'big': 762, 'small': 7934, 'deep': 5840}, 
            'pot': {'red': 7318, 'blue': 5375, 'green': 6443, 'black': 9952, 'white': 3958, 'magenta': 5087, 'big': 9169, 'small': 1386, 'deep': 4363}, 
            'keys': {'red': 7490, 'blue': 105, 'green': 6813, 'black': 7730, 'white': 625, 'magenta': 7427, 'big': 974, 'small': 2171, 'deep': 7714}
            },
        'd':
            {'laptop': {'red': 3512, 'blue': 6812, 'green': 8558, 'black': 575, 'white': 6306, 'magenta': 9795, 'big': 7807,'small': 5917, 'deep': 2796},
            'remote control': {'red': 7311, 'blue': 1527, 'green': 8930, 'black': 9170, 'white': 5904, 'magenta': 2881, 'big': 422, 'small': 5410, 'deep': 7105}, 
            'bowl': {'red': 8490, 'blue': 521, 'green': 6148, 'black': 8690, 'white': 1599, 'magenta': 4007, 'big': 992, 'small': 9131, 'deep':6309}, 
            'spoon': {'red': 7276, 'blue': 8959, 'green': 9149, 'black': 945, 'white': 3553, 'magenta': 5401, 'big': 2304, 'small': 4402, 'deep': 2728}, 
            'fork': {'red': 9708, 'blue': 530, 'green': 6935, 'black': 6207, 'white': 811, 'magenta': 350, 'big': 5064, 'small': 4570, 'deep': 8173}, 
            'pot': {'red': 3217, 'blue': 8191, 'green': 2306, 'black': 1399, 'white': 7616, 'magenta': 8721, 'big': 2120, 'small': 5848, 'deep': 2748}, 
            'keys': {'red': 2084, 'blue': 7880, 'green': 632, 'black': 4419, 'white': 9236, 'magenta': 6435, 'big': 8742, 'small': 7179, 'deep': 1412}
            }
            }

    items = {
        "laptop":{"red","blue","green","black","white","magenta","big","small","deep"},
        "remote control":{"red","blue","green","black","white","magenta","big","small","deep"}, 
        "bowl":{"red","blue","green","black","white","magenta","big","small","deep"},
        "spoon":{"red","blue","green","black","white","magenta","big","small","deep"},
        "fork":{"red","blue","green","black","white","magenta","big","small","deep"},
        "pot":{"red","blue","green","black","white","magenta","big","small","deep"},
        "keys":{"red","blue","green","black","white","magenta","big","small","deep"}
        }
    catagories  = ["laptop", "remote control","bowl", "spoon", "fork","pot","keys"]
    agents_names = ['a','b','c','d']

    # python implementation of the algorithm.
    n_size.append(get_n_size(catagories, items, agents_names))
    data = fair_division_python.Data(catagories,agents_evaluation,items)
    start = time.perf_counter()
    allocation = fair_division_python.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    runntime.append(total_time) 

    # cython (C generated python) implementation of the algorithm.
    start = time.perf_counter()
    allocation = fair_division_cython.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    improved_runntime.append(total_time) 

    # example 4- mid size agent list
    agents_evaluation ={
            'a': {'laptop': {'red': 6908, 'blue': 3858, 'green': 6574, 'black': 2747, 'white': 6002, 'magenta': 3393, 'big': 1645, 'small': 6531, 'deep': 8068}, 
                'remote control': {'red': 7420, 'blue': 8305, 'green': 4659, 'black': 507, 'white': 4471, 'magenta': 5661, 'big': 6058, 'small': 6575, 'deep': 55},
                'bowl': {'red': 7861, 'blue': 349, 'green': 6746, 'black': 791, 'white': 2684, 'magenta': 1325, 'big': 749, 'small': 3370, 'deep': 2588},
                'spoon': {'red': 3362, 'blue': 8427, 'green': 9608, 'black': 6687, 'white': 120, 'magenta': 4790, 'big': 2640, 'small': 8257, 'deep': 1686}, 
                'fork': {'red': 8059, 'blue': 8619, 'green': 3307, 'black': 3203, 'white': 6803, 'magenta': 7244, 'big': 7379, 'small': 1203, 'deep': 7169}, 
                'pot': {'red': 6695, 'blue': 1643, 'green': 9040, 'black': 2846, 'white': 5167, 'magenta': 5567, 'big': 8209, 'small': 9057, 'deep': 3788}, 
                'keys': {'red': 8665, 'blue': 9200, 'green': 6646, 'black': 3785, 'white': 4148, 'magenta': 1936, 'big': 3162, 'small': 5872, 'deep': 9011}
                }, 
            'b': 
                {'laptop': {'red': 6111, 'blue': 8811, 'green': 8034, 'black': 7554, 'white': 5672, 'magenta': 5546, 'big': 1293, 'small': 9936, 'deep': 8467}, 
                'remote control': {'red': 4362, 'blue': 8463, 'green': 8565, 'black': 7627, 'white': 5267, 'magenta': 6592, 'big': 554, 'small': 1829, 'deep': 3636}, 
                'bowl': {'red': 4169, 'blue': 4175, 'green': 3113, 'black': 7924, 'white': 6111, 'magenta': 7322, 'big': 6171, 'small': 7318, 'deep': 4497},
                'spoon': {'red': 5966, 'blue': 9823, 'green': 426, 'black': 1414, 'white': 6609, 'magenta': 9917, 'big': 6350, 'small': 6108, 'deep': 5227}, 
                'fork': {'red': 9797, 'blue': 548, 'green': 4136, 'black': 7491, 'white': 3048, 'magenta': 7145, 'big': 7018, 'small': 7932, 'deep': 5235}, 
                'pot': {'red': 6145, 'blue': 5779, 'green': 6570, 'black': 3128, 'white': 3651, 'magenta': 5554, 'big': 1211, 'small': 4787, 'deep': 2831},
                'keys': {'red': 4877, 'blue': 393, 'green': 7050, 'black': 1196, 'white': 2793, 'magenta': 237, 'big': 5836, 'small': 2914, 'deep': 2291}
                }, 
            'c': 
                {'laptop': {'red': 7399, 'blue': 946, 'green': 7899, 'black': 9337, 'white': 2825, 'magenta': 5032, 'big': 6405, 'small': 5753, 'deep': 7157},
                'remote control': {'red': 4585, 'blue': 6450, 'green': 8638, 'black': 2113, 'white': 2568, 'magenta': 1234, 'big': 8135, 'small': 9760, 'deep': 143}, 
                'bowl': {'red': 9823, 'blue': 6379, 'green': 9981, 'black': 2162, 'white': 1580, 'magenta': 4709, 'big': 6075, 'small': 510, 'deep': 5285},
                'spoon': {'red': 239, 'blue': 6216, 'green': 5495, 'black': 511, 'white': 8595, 'magenta': 979, 'big': 3335, 'small': 576, 'deep': 7619}, 
                'fork': {'red': 2169, 'blue': 9310, 'green': 5304, 'black': 7750, 'white': 5835, 'magenta': 1146, 'big': 4374, 'small': 2092, 'deep': 7076},
                'pot': {'red': 7657, 'blue': 5044, 'green': 185, 'black': 1421, 'white': 8935, 'magenta': 9251, 'big': 4564, 'small': 1102, 'deep': 9964}, 
                'keys': {'red': 8510, 'blue': 317, 'green': 2608, 'black': 2668, 'white': 7499, 'magenta': 6822, 'big': 3396, 'small': 2800, 'deep': 1804}
                },
            'd':
                {'laptop': {'red': 7483, 'blue': 2096, 'green': 8251, 'black': 7013, 'white': 4197, 'magenta': 884, 'big': 3384, 'small': 2450, 'deep': 414},
                'remote control': {'red': 9743, 'blue': 9237, 'green': 7023, 'black': 6886, 'white': 6911, 'magenta': 117, 'big': 1063, 'small': 4927, 'deep': 7354},
                'bowl': {'red': 2213, 'blue': 4969, 'green': 1869, 'black': 4015, 'white': 1860, 'magenta': 5839, 'big': 4495, 'small': 3633, 'deep': 3857},
                'spoon': {'red': 3349, 'blue': 7725, 'green': 262, 'black': 6883, 'white': 7930, 'magenta': 2686, 'big': 8356, 'small': 8353, 'deep': 5738}, 
                'fork': {'red': 5379, 'blue': 4209, 'green': 1725, 'black': 8815, 'white': 5159, 'magenta': 4063, 'big': 8796, 'small': 5619, 'deep': 5993},
                'pot': {'red': 446, 'blue': 2355, 'green': 9555, 'black': 1239, 'white': 5868, 'magenta': 4059, 'big': 5824, 'small': 3494, 'deep': 658},
                'keys': {'red': 6724, 'blue': 2449, 'green': 2506, 'black': 5718, 'white': 8686, 'magenta': 1729, 'big': 2209, 'small': 4341, 'deep': 668}
                }, 
            'e': {'laptop': {'red': 8725, 'blue': 2963, 'green': 239, 'black': 5444, 'white': 3278, 'magenta': 9242, 'big': 5645, 'small': 8258, 'deep': 2421},
                'remote control': {'red': 9320, 'blue': 8733, 'green': 9513, 'black': 7784, 'white': 7429, 'magenta': 3261, 'big': 4663, 'small': 6549, 'deep': 2874},
                'bowl': {'red': 4242, 'blue': 5800, 'green': 3527, 'black': 948, 'white': 6238, 'magenta': 8848, 'big': 5444, 'small': 3603, 'deep': 8360}, 
                'spoon': {'red': 1521, 'blue': 7011, 'green': 2114, 'black': 2315, 'white': 6498, 'magenta': 6380, 'big': 650, 'small': 1914, 'deep': 2936}, 
                'fork': {'red': 236, 'blue': 5108, 'green': 7028, 'black': 2672, 'white': 3721, 'magenta': 9895, 'big': 5438, 'small': 543, 'deep': 5108}, 
                'pot': {'red': 7002, 'blue': 3790, 'green': 1228, 'black': 3981, 'white': 5859, 'magenta': 2911, 'big': 3250, 'small': 4112, 'deep': 257},
                'keys': {'red': 4967, 'blue': 9725, 'green': 1964, 'black': 9583, 'white': 3157, 'magenta': 4002, 'big': 3653, 'small': 2236, 'deep': 8108}
                }, 
            'f': {'laptop': {'red': 7529, 'blue': 2433, 'green': 7789, 'black': 266, 'white': 7077, 'magenta': 6072, 'big': 6849, 'small': 7611, 'deep': 162},
                'remote control': {'red': 7160, 'blue': 6480, 'green': 4315, 'black': 4175, 'white': 9405, 'magenta': 8868, 'big': 7225, 'small': 4714, 'deep': 9441},
                'bowl': {'red': 9514, 'blue': 1361, 'green': 6932, 'black': 3511, 'white': 5716, 'magenta': 8417, 'big': 3213, 'small': 3557, 'deep': 3093},
                'spoon': {'red': 8863, 'blue': 7747, 'green': 151, 'black': 6459, 'white': 7470, 'magenta': 7449, 'big': 6292, 'small': 159, 'deep': 4063}, 
                'fork': {'red': 1011, 'blue': 1848, 'green': 1705, 'black': 5175, 'white': 191, 'magenta': 6586, 'big': 8409, 'small': 1671, 'deep': 4581},
                'pot': {'red': 483, 'blue': 7281, 'green': 6718, 'black': 8538, 'white': 7245, 'magenta': 797, 'big': 6697, 'small': 2512, 'deep': 5428},
                'keys': {'red': 2265, 'blue': 4811, 'green': 9411, 'black': 4700, 'white': 5102, 'magenta': 5330, 'big': 9569, 'small': 9729, 'deep': 9719}
                }, 
            'G': {'laptop': {'red': 3329, 'blue': 846, 'green': 8169, 'black': 2194, 'white': 3771,'magenta': 8120, 'big': 5517, 'small': 4177, 'deep': 2329}, 
                'remote control': {'red': 3590, 'blue': 8598, 'green': 7733, 'black': 962, 'white': 7269, 'magenta': 5319, 'big': 1969, 'small': 5401, 'deep': 2658},
                'bowl': {'red': 893, 'blue': 3943, 'green': 4476, 'black': 9021, 'white': 7189, 'magenta': 254, 'big': 1486, 'small': 6686, 'deep': 5843}, 
                'spoon': {'red': 2718, 'blue': 7471, 'green': 7783, 'black': 3475, 'white': 1902, 'magenta': 7193, 'big': 2777, 'small': 1184, 'deep': 7266},
                'fork': {'red': 4692, 'blue': 896, 'green': 8580, 'black': 1971, 'white': 3885, 'magenta': 6322, 'big': 6618, 'small': 1367, 'deep': 6682}, 
                'pot': {'red': 6698, 'blue': 3981, 'green': 512, 'black': 8626, 'white': 634, 'magenta': 5402, 'big': 2247, 'small': 1678, 'deep': 7530},
                'keys': {'red': 7755, 'blue': 6266, 'green': 5596, 'black': 4091, 'white': 3010, 'magenta': 5987, 'big': 2411, 'small': 6579, 'deep': 942}
                }
            }

    items = {
        "laptop":{"red","blue","green","black","white","magenta","big","small","deep"},
        "remote control":{"red","blue","green","black","white","magenta","big","small","deep"}, 
        "bowl":{"red","blue","green","black","white","magenta","big","small","deep"},
        "spoon":{"red","blue","green","black","white","magenta","big","small","deep"},
        "fork":{"red","blue","green","black","white","magenta","big","small","deep"},
        "pot":{"red","blue","green","black","white","magenta","big","small","deep"},
        "keys":{"red","blue","green","black","white","magenta","big","small","deep"}
        }
    catagories  = ["laptop", "remote control","bowl", "spoon", "fork","pot","keys"]
    agents_names = ['a','b','c','d','e','f','G']

    # python implementation of the algorithm.
    n_size.append(get_n_size(catagories, items, agents_names))
    data = fair_division_python.Data(catagories,agents_evaluation,items)
    start = time.perf_counter()
    allocation = fair_division_python.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    runntime.append(total_time)

    # cython (C generated python) implementation of the algorithm.
    start = time.perf_counter()
    allocation = fair_division_cython.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    improved_runntime.append(total_time)

    # example 4- big size agent list and items
    agents_evaluation ={
        "a":{"laptop":{"red":383359,"blue":423474,"green":6473,"black":236676,"white":620772, "magenta":644491,"big":184259, "small":11945, "deep":336684, "large":138372, "huge":578646, "purple":690474, "orange":56984, "soft":690656},
            "remote control":{ "red":167561, "blue":672934, "green":91255, "black":296509, "white":42550, "magenta":644687, "big":886150, "small":218151, "deep":142816, "large":27732, "huge":378922, "purple":365032, "orange":570504, "soft":339857 },
            "bowl":{ "red":890043, "blue":905339, "green":352149, "black":665771, "white":524042, "magenta":160652, "big":401694, "small":540792, "deep":810637, "large":588617, "huge":409553, "purple":289315, "orange":940631, "soft":902924 },
            "spoon":{ "red":492806, "blue":409498, "green":879530, "black":148155, "white":641269, "magenta":950779, "big":124039, "small":728803, "deep":650968, "large":651303, "huge":197940, "purple":55169, "orange":548178, "soft":342074 },
            "fork":{ "red":991776, "blue":37002, "green":831854, "black":782338, "white":833555, "magenta":853721, "big":311186, "small":938437, "deep":965155, "large":94629, "huge":164458, "purple":390475, "orange":831246, "soft":968171 },
            "pot":{ "red":619216, "blue":579873, "green":383572, "black":717606, "white":158918, "magenta":871355, "big":649118, "small":345726, "deep":872728, "large":259413, "huge":986201, "purple":65566, "orange":653564, "soft":35256 },
            "cable":{ "red":953410, "blue":631491, "green":137547, "black":122654, "white":903511, "magenta":351107, "big":605681, "small":666586, "deep":287605, "large":642792, "huge":642140, "purple":204855, "orange":578991, "soft":587366 },
            "case":{ "red":403171, "blue":705538, "green":176442, "black":146214, "white":442727, "magenta":857332, "big":540907, "small":679112, "deep":344553, "large":676878, "huge":179171, "purple":627534, "orange":440835, "soft":865493 },
            "music":{ "red":316997, "blue":771182, "green":321301, "black":872143, "white":75474, "magenta":47473, "big":845783, "small":575620, "deep":392005, "large":492942, "huge":452207, "purple":175771, "orange":485447, "soft":827560 },
            "bike":{ "red":939853, "blue":658932, "green":92962, "black":434527, "white":195108, "magenta":211052, "big":35225, "small":607956, "deep":698879, "large":565468, "huge":290055, "purple":731653, "orange":777450, "soft":432258 },
            "hamburger":{ "red":708689, "blue":945006, "green":298197, "black":340650, "white":363170, "magenta":594303, "big":855106, "small":48246, "deep":475076, "large":946784, "huge":948491, "purple":683753, "orange":643001, "soft":853581 },
            "pizza":{ "red":639573, "blue":629238, "green":46487, "black":387709, "white":511722, "magenta":221266, "big":352375, "small":372522, "deep":225939, "large":783089, "huge":23661, "purple":375675, "orange":445670, "soft":426475 },
            "keys":{ "red":412097, "blue":308517, "green":368678, "black":958651, "white":370517, "magenta":984331, "big":246662, "small":998954, "deep":432333, "large":779744, "huge":490126, "purple":959740, "orange":673726, "soft":427599 }
        },
        "b":
            {"laptop":{ "red":261513, "blue":853419, "green":616803, "black":703326, "white":721927, "magenta":80000, "big":774650, "small":562666, "deep":542217, "large":939166, "huge":231677, "purple":41033, "orange":540960, "soft":111560 },
            "remote control":{ "red":867278, "blue":440270, "green":192822, "black":257559, "white":616870, "magenta":287116, "big":878537, "small":656079, "deep":676849, "large":481530, "huge":184848, "purple":868654, "orange":415997, "soft":791223 },
            "bowl":{ "red":658892, "blue":114565, "green":757479, "black":72113, "white":370430, "magenta":711458, "big":868808, "small":707925, "deep":918074, "large":242727, "huge":49499, "purple":151146, "orange":51519, "soft":147134 },
            "spoon":{ "red":714486, "blue":192628, "green":731455, "black":782219, "white":533265, "magenta":678743, "big":781778, "small":711185, "deep":542575, "large":722643, "huge":343831, "purple":538796, "orange":872276, "soft":446798 },
            "fork":{ "red":953716, "blue":800162, "green":670225, "black":525028, "white":167094, "magenta":355689, "big":179559, "small":39367, "deep":70959, "large":237975, "huge":499026, "purple":346583, "orange":324911, "soft":154588 },
            "pot":{ "red":73934, "blue":19946, "green":885924, "black":685144, "white":911626, "magenta":698195, "big":615302, "small":978682, "deep":743346, "large":408095, "huge":607498, "purple":310379, "orange":206039, "soft":791498 },
            "cable":{ "red":714355, "blue":881788, "green":255389, "black":206444, "white":111501, "magenta":721910, "big":527038, "small":875424, "deep":680346, "large":501776, "huge":128992, "purple":239333, "orange":929581, "soft":743366 },
            "case":{ "red":176585, "blue":998609, "green":401002, "black":871025, "white":636091, "magenta":950305, "big":538548, "small":475074, "deep":378309, "large":854520, "huge":102025, "purple":922343, "orange":659524, "soft":441684 },
            "music":{ "red":197563, "blue":720991, "green":694844, "black":654544, "white":378653, "magenta":737358, "big":823579, "small":644703, "deep":559833, "large":108218, "huge":881197, "purple":556773, "orange":379343, "soft":236574 },
            "bike":{ "red":710076, "blue":874868, "green":25462, "black":887835, "white":26008, "magenta":282008, "big":991282, "small":105301, "deep":502153, "large":693819, "huge":847283, "purple":602060, "orange":589087, "soft":958540 },
            "hamburger":{ "red":52839, "blue":467323, "green":753958, "black":827591, "white":72943, "magenta":568638, "big":771326, "small":918743, "deep":45478, "large":274019, "huge":588099, "purple":947412, "orange":240895, "soft":238538 },
            "pizza":{ "red":99093, "blue":173401, "green":899014, "black":965933, "white":214356, "magenta":938494, "big":971875, "small":367540, "deep":244321, "large":189537, "huge":914246, "purple":84001, "orange":445285, "soft":758435 },
            "keys":{ "red":361383, "blue":943519, "green":449066, "black":284853, "white":713036, "magenta":549957, "big":254778, "small":508985, "deep":295822, "large":21920, "huge":120063, "purple":255042, "orange":303908, "soft":177851 }
        },
        "c":
            {"laptop":{ "red":182990, "blue":443210, "green":41609, "black":816815, "white":716030, "magenta":118288, "big":239544, "small":359600, "deep":737453, "large":813570, "huge":569884, "purple":359226, "orange":733776, "soft":810935 },
            "remote control":{ "red":93103, "blue":860140, "green":734920, "black":487058, "white":856890, "magenta":575565, "big":967117, "small":26830, "deep":2730, "large":287072, "huge":175899, "purple":751990, "orange":410746, "soft":728725 },
            "bowl":{ "red":936667, "blue":884488, "green":701077, "black":655577, "white":912036, "magenta":725869, "big":747145, "small":736726, "deep":656363, "large":299359, "huge":959847, "purple":383869, "orange":420994, "soft":364717 },
            "spoon":{ "red":57210, "blue":227371, "green":787624, "black":720702, "white":129105, "magenta":794136, "big":416808, "small":565568, "deep":974609, "large":873699, "huge":359249, "purple":743155, "orange":276800, "soft":46520 },
            "fork":{ "red":603896, "blue":771642, "green":663637, "black":621658, "white":237297, "magenta":578676, "big":183640, "small":327913, "deep":212607, "large":494208, "huge":940717, "purple":839199, "orange":157050, "soft":811226 },
            "pot":{ "red":646401, "blue":361922, "green":829795, "black":295846, "white":894138, "magenta":472144, "big":327521, "small":606058, "deep":450826, "large":417080, "huge":529910, "purple":476122, "orange":297250, "soft":723285 },
            "cable":{ "red":40207, "blue":483237, "green":679347, "black":841816, "white":528585, "magenta":846432, "big":229420, "small":336472, "deep":831367, "large":124976, "huge":230311, "purple":958750, "orange":381210, "soft":149902 },
            "case":{ "red":402099, "blue":337454, "green":863956, "black":13743, "white":508473, "magenta":131880, "big":795670, "small":38221, "deep":733242, "large":193599, "huge":978302, "purple":538130, "orange":129067, "soft":329678 },
            "music":{ "red":459279, "blue":217506, "green":668232, "black":269726, "white":760748, "magenta":944255, "big":335384, "small":157909, "deep":997563, "large":865416, "huge":129457, "purple":26887, "orange":967342, "soft":325452 },
            "bike":{ "red":770796, "blue":198273, "green":689548, "black":413552, "white":274627, "magenta":454143, "big":257071, "small":418921, "deep":841028, "large":104906, "huge":530420, "purple":332194, "orange":944081, "soft":426231 },
            "hamburger":{ "red":978056, "blue":151230, "green":276747, "black":966549, "white":301567, "magenta":287913, "big":581634, "small":679999, "deep":258000, "large":795415, "huge":819913, "purple":234463, "orange":580882, "soft":230843 },
            "pizza":{ "red":928016, "blue":63138, "green":426553, "black":177432, "white":676726, "magenta":616479, "big":266756, "small":994759, "deep":621953, "large":753288, "huge":998907, "purple":362912, "orange":616262, "soft":870504 },
            "keys":{ "red":960486, "blue":561931, "green":409769, "black":274840, "white":723644, "magenta":864202, "big":201508, "small":789138, "deep":539887, "large":931349, "huge":843129, "purple":265946, "orange":645316, "soft":472658 }
        },
        "d":
            {"laptop":{ "red":803666, "blue":213697, "green":667431, "black":339879, "white":573564, "magenta":808788, "big":418616, "small":794276, "deep":696719, "large":826784, "huge":470642, "purple":582772, "orange":375375, "soft":659699 },
            "remote control":{ "red":36025, "blue":306190, "green":590144, "black":103379, "white":665921, "magenta":251219, "big":14141, "small":390691, "deep":321003, "large":238661, "huge":850166, "purple":422793, "orange":613632, "soft":99824 },
            "bowl":{ "red":411372, "blue":497278, "green":256065, "black":607322, "white":647263, "magenta":84618, "big":330224, "small":664710, "deep":498904, "large":382611, "huge":783583, "purple":526270, "orange":987991, "soft":867010 },
            "spoon":{ "red":378515, "blue":511398, "green":57417, "black":368637, "white":486309, "magenta":672164, "big":188983, "small":334229, "deep":247843, "large":624471, "huge":820243, "purple":726907, "orange":211259, "soft":467882 },
            "fork":{ "red":849425, "blue":716730, "green":605694, "black":881773, "white":132561, "magenta":929329, "big":552868, "small":304789, "deep":182485, "large":675304, "huge":567530, "purple":528159, "orange":409071, "soft":596209 },
            "pot":{ "red":878769, "blue":341782, "green":814281, "black":728890, "white":186611, "magenta":969555, "big":676702, "small":139002, "deep":469115, "large":915884, "huge":439039, "purple":766997, "orange":860766, "soft":45873 },
            "cable":{ "red":120644, "blue":940658, "green":776432, "black":724151, "white":264558, "magenta":684098, "big":423691, "small":462288, "deep":795899, "large":707202, "huge":634532, "purple":11010, "orange":180835, "soft":557427 },
            "case":{ "red":618957, "blue":120262, "green":120959, "black":663871, "white":168393, "magenta":250394, "big":439031, "small":909389, "deep":167331, "large":795553, "huge":879500, "purple":576886, "orange":13956, "soft":66707 },
            "music":{ "red":601385, "blue":279059, "green":497786, "black":288737, "white":903561, "magenta":406242, "big":257868, "small":958511, "deep":162608, "large":363857, "huge":89138, "purple":970030, "orange":387462, "soft":331027 },
            "bike":{ "red":582723, "blue":629824, "green":463851, "black":900124, "white":431717, "magenta":783886, "big":570762, "small":638706, "deep":133053, "large":691871, "huge":394830, "purple":840553, "orange":740498, "soft":144758 },
            "hamburger":{ "red":185271, "blue":657279, "green":33840, "black":724905, "white":766236, "magenta":518816, "big":470473, "small":576315, "deep":983890, "large":763698, "huge":607320, "purple":390135, "orange":959371, "soft":450076 },
            "pizza":{ "red":7317, "blue":473972, "green":463327, "black":161040, "white":719158, "magenta":551017, "big":233712, "small":122188, "deep":880772, "large":696931, "huge":111426, "purple":740747, "orange":854694, "soft":158369 },
            "keys":{ "red":440380, "blue":392031, "green":92439, "black":685535, "white":720460, "magenta":285152, "big":87440, "small":568682, "deep":142998, "large":373964, "huge":9516, "purple":956059, "orange":278835, "soft":964735 }
        },
        "e":
            {"laptop":{ "red":73576, "blue":813966, "green":610222, "black":981904, "white":586645, "magenta":672118, "big":377304, "small":284528, "deep":96413, "large":335429, "huge":616917, "purple":968892, "orange":41434, "soft":984350 },
            "remote control":{ "red":731706, "blue":435901, "green":628322, "black":234693, "white":926336, "magenta":517868, "big":979394, "small":497665, "deep":658830, "large":850819, "huge":248686, "purple":929164, "orange":26210, "soft":785825 },
            "bowl":{ "red":645644, "blue":61979, "green":47993, "black":560509, "white":891321, "magenta":801651, "big":787160, "small":69563, "deep":329777, "large":855634, "huge":923423, "purple":479928, "orange":655876, "soft":199111 },
            "spoon":{ "red":432485, "blue":644287, "green":909703, "black":32781, "white":810101, "magenta":581910, "big":588863, "small":842540, "deep":173162, "large":126322, "huge":866719, "purple":486381, "orange":259291, "soft":219814 },
            "fork":{ "red":201328, "blue":611990, "green":124425, "black":385342, "white":346246, "magenta":506171, "big":180062, "small":222931, "deep":190066, "large":124307, "huge":499653, "purple":906519, "orange":897371, "soft":236760 },
            "pot":{ "red":800683, "blue":724792, "green":811869, "black":711303, "white":718346, "magenta":783534, "big":820401, "small":606573, "deep":621524, "large":831323, "huge":163506, "purple":162975, "orange":343303, "soft":854747 },
            "cable":{ "red":154365, "blue":769387, "green":884290, "black":387886, "white":240973, "magenta":41650, "big":157581, "small":4432, "deep":916589, "large":68129, "huge":342122, "purple":297878, "orange":993178, "soft":900481 },
            "case":{ "red":270440, "blue":657017, "green":98875, "black":308509, "white":372619, "magenta":895923, "big":633968, "small":478259, "deep":554158, "large":765591, "huge":467245, "purple":817819, "orange":6274, "soft":803918 },
            "music":{ "red":592808, "blue":551054, "green":969713, "black":604444, "white":376363, "magenta":650942, "big":346143, "small":503593, "deep":321210, "large":659393, "huge":727093, "purple":442394, "orange":979487, "soft":658967 },
            "bike":{ "red":201310, "blue":157626, "green":841344, "black":564535, "white":348990, "magenta":694380, "big":448891, "small":284463, "deep":874709, "large":58442, "huge":784648, "purple":761821, "orange":766105, "soft":238135 },
            "hamburger":{ "red":451680, "blue":175327, "green":344112, "black":696197, "white":912079, "magenta":28892, "big":149006, "small":919941, "deep":145311, "large":64208, "huge":372941, "purple":571075, "orange":156215, "soft":838300 },
            "pizza":{ "red":93964, "blue":84426, "green":272698, "black":357076, "white":67431, "magenta":959579, "big":132681, "small":354815, "deep":715879, "large":545665, "huge":49141, "purple":610077, "orange":841640, "soft":214068 },
            "keys":{ "red":379108, "blue":543416, "green":716985, "black":611029, "white":248884, "magenta":725701, "big":30890, "small":685524, "deep":579075, "large":957145, "huge":443749, "purple":626015, "orange":537291, "soft":443103 }
        },
        "f":
            {"laptop":{ "red":681721, "blue":732881, "green":304212, "black":877805, "white":557119, "magenta":929574, "big":589015, "small":907918, "deep":684853, "large":278347, "huge":910653, "purple":548489, "orange":949981, "soft":247476 },
            "remote control":{ "red":685685, "blue":906911, "green":313837, "black":481550, "white":710824, "magenta":818079, "big":417037, "small":230093, "deep":657420, "large":792039, "huge":874413, "purple":564736, "orange":22753, "soft":934014 },
            "bowl":{ "red":683490, "blue":347594, "green":840415, "black":363311, "white":576278, "magenta":784823, "big":675634, "small":9028, "deep":873784, "large":938625, "huge":182393, "purple":338517, "orange":119581, "soft":340722 },
            "spoon":{ "red":382416, "blue":553087, "green":514027, "black":240734, "white":559124, "magenta":112175, "big":916386, "small":698469, "deep":552695, "large":32329, "huge":596348, "purple":356472, "orange":550953, "soft":509607 },
            "fork":{ "red":987100, "blue":684192, "green":499336, "black":496987, "white":596434, "magenta":172791, "big":743357, "small":868073, "deep":840284, "large":880108, "huge":71817, "purple":744949, "orange":545534, "soft":622139 },
            "pot":{ "red":289972, "blue":662964, "green":41655, "black":518813, "white":805925, "magenta":617928, "big":176206, "small":520825, "deep":634678, "large":558255, "huge":703014, "purple":592753, "orange":481902, "soft":494052 },
            "cable":{ "red":655283, "blue":902314, "green":759855, "black":400814, "white":572699, "magenta":838527, "big":940345, "small":635384, "deep":505881, "large":408694, "huge":386482, "purple":864804, "orange":101150, "soft":299712 },
            "case":{ "red":868542, "blue":742564, "green":552724, "black":761603, "white":948985, "magenta":508622, "big":108826, "small":852270, "deep":77840, "large":199542, "huge":123307, "purple":479968, "orange":762279, "soft":9370 },
            "music":{ "red":991068, "blue":88124, "green":824108, "black":987565, "white":563292, "magenta":309054, "big":685524, "small":515661, "deep":331445, "large":220051, "huge":25336, "purple":273086, "orange":316659, "soft":754649 },
            "bike":{ "red":823601, "blue":16422, "green":14525, "black":687660, "white":369687, "magenta":161728, "big":731752, "small":853865, "deep":549147, "large":215847, "huge":841063, "purple":984676, "orange":303443, "soft":19364 },
            "hamburger":{ "red":664087, "blue":240028, "green":153961, "black":555113, "white":518622, "magenta":577042, "big":162033, "small":708681, "deep":10635, "large":448889, "huge":485150, "purple":145944, "orange":49856, "soft":150202 },
            "pizza":{ "red":110881, "blue":933268, "green":806114, "black":529279, "white":601877, "magenta":760892, "big":939336, "small":95619, "deep":405828, "large":827163, "huge":423488, "purple":432976, "orange":941177, "soft":228713 },
            "keys":{ "red":46145, "blue":462275, "green":747534, "black":119927, "white":194887, "magenta":437054, "big":407560, "small":747408, "deep":185090, "large":985931, "huge":201171, "purple":15001, "orange":387098, "soft":397048 }
        },
        "G":{
            "laptop":{ "red":574695, "blue":790254, "green":494409, "black":851927, "white":913240, "magenta":191691, "big":67644, "small":373035, "deep":944116, "large":808078, "huge":133753, "purple":548005, "orange":805691, "soft":150150 },
            "remote control":{ "red":589565, "blue":266512, "green":473174, "black":889653, "white":973697, "magenta":806421, "big":501464, "small":836114, "deep":254274, "large":803744, "huge":378907, "purple":558367, "orange":362174, "soft":327149 },
            "bowl":{ "red":109200, "blue":170912, "green":984025, "black":483274, "white":284841, "magenta":974411, "big":646858, "small":420195, "deep":325580, "large":979610, "huge":430093, "purple":722238, "orange":111740, "soft":464663 },
            "spoon":{ "red":909810, "blue":910133, "green":601698, "black":387439, "white":138006, "magenta":35422, "big":462322, "small":994445, "deep":447459, "large":563683, "huge":722177, "purple":393081, "orange":131776, "soft":381780 },
            "fork":{ "red":317590, "blue":888572, "green":525823, "black":884162, "white":216503, "magenta":442206, "big":574432, "small":973284, "deep":910977, "large":26646, "huge":257435, "purple":955209, "orange":112914, "soft":373314 },
            "pot":{ "red":689, "blue":499277, "green":440129, "black":551522, "white":997865, "magenta":806270, "big":238967, "small":228166, "deep":439104, "large":876245, "huge":308844, "purple":797793, "orange":961517, "soft":850773 },
            "cable":{ "red":781337, "blue":668027, "green":839885, "black":780845, "white":531801, "magenta":265429, "big":782201, "small":951626, "deep":797682, "large":633526, "huge":210740, "purple":651053, "orange":392061, "soft":310105 },
            "case":{ "red":142573, "blue":838216, "green":316057, "black":378798, "white":331961, "magenta":628662, "big":320131, "small":224066, "deep":948843, "large":263894, "huge":844472, "purple":601711, "orange":861332, "soft":784740 },
            "music":{ "red":432278, "blue":462053, "green":295541, "black":259632, "white":495007, "magenta":471836, "big":409487, "small":194998, "deep":252477, "large":53351, "huge":963017, "purple":635801, "orange":758944, "soft":964348 },
            "bike":{ "red":52261, "blue":533029, "green":514994, "black":218338, "white":310381, "magenta":52888, "big":88860, "small":773663, "deep":673630, "large":57725, "huge":374473, "purple":368097, "orange":147816, "soft":832602 },
            "hamburger":{ "red":708443, "blue":548428, "green":525979, "black":208180, "white":466510, "magenta":787077, "big":55369, "small":930517, "deep":666617, "large":701771, "huge":126990, "purple":493192, "orange":178944, "soft":830745 },
            "pizza":{ "red":363434, "blue":105296, "green":37772, "black":370546, "white":267536, "magenta":953549, "big":732761, "small":167016, "deep":760718, "large":620999, "huge":695050, "purple":847077, "orange":229538, "soft":50368 },
            "keys":{ "red":180252, "blue":994349, "green":275053, "black":894942, "white":757018, "magenta":76250, "big":502605, "small":705253, "deep":214507, "large":971957, "huge":657654, "purple":561276, "orange":899448, "soft":692514 }
        },
        "h":
            {"laptop":{ "red":775581, "blue":880732, "green":939340, "black":346260, "white":555819, "magenta":420225, "big":57240, "small":743648, "deep":785596, "large":569599, "huge":431059, "purple":584157, "orange":295103, "soft":841230 },
            "remote control":{ "red":31054, "blue":170323, "green":881066, "black":553902, "white":496200, "magenta":858599, "big":79278, "small":735661, "deep":325679, "large":307596, "huge":995564, "purple":521798, "orange":336725, "soft":722602 },
            "bowl":{ "red":220693, "blue":418570, "green":86200, "black":858455, "white":385628, "magenta":424158, "big":215828, "small":966765, "deep":592432, "large":954584, "huge":282881, "purple":171725, "orange":58920, "soft":333890 },
            "spoon":{ "red":838539, "blue":586731, "green":695219, "black":591994, "white":773138, "magenta":471024, "big":579456, "small":696466, "deep":798028, "large":250717, "huge":770006, "purple":38250, "orange":90047, "soft":882007 },
            "fork":{ "red":943237, "blue":695414, "green":423898, "black":765299, "white":564749, "magenta":205125, "big":760495, "small":725626, "deep":945057, "large":30159, "huge":62558, "purple":400072, "orange":644855, "soft":636735 },
            "pot":{ "red":456377, "blue":325605, "green":364139, "black":333987, "white":37572, "magenta":105020, "big":315031, "small":922509, "deep":635842, "large":560209, "huge":403385, "purple":625360, "orange":179427, "soft":236529 },
            "cable":{ "red":917956, "blue":276915, "green":731740, "black":896039, "white":316938, "magenta":82259, "big":655913, "small":898598, "deep":546821, "large":907880, "huge":174943, "purple":589223, "orange":852556, "soft":102575 },
            "case":{ "red":222159, "blue":394915, "green":853698, "black":827288, "white":151120, "magenta":211358, "big":726131, "small":499212, "deep":761191, "large":222635, "huge":65991, "purple":197606, "orange":706886, "soft":347318 },
            "music":{ "red":389044, "blue":262788, "green":163483, "black":417323, "white":642952, "magenta":229313, "big":482295, "small":283465, "deep":743623, "large":726863, "huge":858994, "purple":257, "orange":78952, "soft":872661 },
            "bike":{ "red":539028, "blue":893994, "green":629973, "black":868722, "white":130133, "magenta":112507, "big":116013, "small":243179, "deep":941244, "large":542177, "huge":657124, "purple":78419, "orange":501894, "soft":641615 },
            "hamburger":{ "red":854026, "blue":899500, "green":955709, "black":533682, "white":595602, "magenta":549121, "big":13472, "small":424236, "deep":397885, "large":758976, "huge":839490, "purple":14311, "orange":75912, "soft":858367 },
            "pizza":{ "red":662381, "blue":396504, "green":334281, "black":124143, "white":744244, "magenta":383536, "big":791233, "small":381858, "deep":661708, "large":751461, "huge":229271, "purple":574480, "orange":656440, "soft":110920 },
            "keys":{ "red":421891, "blue":548986, "green":966760, "black":908361, "white":750203, "magenta":497058, "big":632776, "small":208547, "deep":542150, "large":607427, "huge":429934, "purple":862799, "orange":45261, "soft":849736 }
        },
        "i":
            {"laptop":{ "red":51443, "blue":645787, "green":172771, "black":385557, "white":924583, "magenta":578401, "big":859223, "small":487362, "deep":1046, "large":303213, "huge":519770, "purple":28949, "orange":725384, "soft":733743 },
            "remote control":{ "red":489382, "blue":930120, "green":85316, "black":806338, "white":431741, "magenta":843784, "big":871168, "small":728965, "deep":835621, "large":609455, "huge":629265, "purple":471215, "orange":775292, "soft":449598 },
            "bowl":{ "red":737153, "blue":830911, "green":453859, "black":160259, "white":431595, "magenta":330401, "big":739500, "small":155163, "deep":61953, "large":693383, "huge":811708, "purple":802115, "orange":850423, "soft":670429 },
            "spoon":{ "red":684114, "blue":884492, "green":590590, "black":487808, "white":104181, "magenta":69392, "big":909197, "small":204220, "deep":726476, "large":381571, "huge":730159, "purple":888869, "orange":725165, "soft":350111 },
            "fork":{ "red":641053, "blue":408247, "green":529549, "black":215160, "white":137195, "magenta":109664, "big":53762, "small":451913, "deep":921221, "large":976912, "huge":762990, "purple":930739, "orange":304710, "soft":165757 },
            "pot":{ "red":772796, "blue":911385, "green":288361, "black":297708, "white":179618, "magenta":396185, "big":579018, "small":7830, "deep":361749, "large":526248, "huge":510174, "purple":515431, "orange":817006, "soft":24226 },
            "cable":{ "red":742247, "blue":653180, "green":828684, "black":736797, "white":439785, "magenta":110194, "big":599547, "small":276455, "deep":697216, "large":763822, "huge":385526, "purple":459626, "orange":848371, "soft":306832 },
            "case":{ "red":947154, "blue":520862, "green":22513, "black":786469, "white":675593, "magenta":327354, "big":601019, "small":712945, "deep":777385, "large":503713, "huge":747771, "purple":873555, "orange":421685, "soft":717232 },
            "music":{ "red":403641, "blue":847295, "green":77890, "black":348557, "white":935579, "magenta":540455, "big":36223, "small":600762, "deep":575392, "large":104829, "huge":334227, "purple":552448, "orange":736962, "soft":66121 },
            "bike":{ "red":744065, "blue":737166, "green":654441, "black":196308, "white":758151, "magenta":360685, "big":10614, "small":386677, "deep":920586, "large":582097, "huge":130475, "purple":836942, "orange":555117, "soft":226892 },
            "hamburger":{ "red":948588, "blue":526655, "green":292122, "black":680588, "white":69953, "magenta":115384, "big":789180, "small":857333, "deep":507830, "large":394080, "huge":547779, "purple":17685, "orange":961902, "soft":413125 },
            "pizza":{ "red":58569, "blue":472416, "green":50662, "black":931249, "white":127644, "magenta":983451, "big":882637, "small":542913, "deep":94952, "large":492658, "huge":464454, "purple":784823, "orange":264412, "soft":793545 },
            "keys":{ "red":427080, "blue":362164, "green":524134, "black":940979, "white":76258, "magenta":319081, "big":986337, "small":498573, "deep":964995, "large":692214, "huge":773664, "purple":588865, "orange":594534, "soft":429584 }
        },
        "j":
            {"laptop":{ "red":952690, "blue":89992, "green":443257, "black":107401, "white":625088, "magenta":10327, "big":157326, "small":290533, "deep":591715, "large":106083, "huge":298066, "purple":716419, "orange":494267, "soft":44474 },
            "remote control":{ "red":207446, "blue":461333, "green":618761, "black":283559, "white":776536, "magenta":249683, "big":284369, "small":245515, "deep":713068, "large":3467, "huge":821934, "purple":944109, "orange":736047, "soft":751450 },
            "bowl":{ "red":853347, "blue":19292, "green":59828, "black":192679, "white":737877, "magenta":438904, "big":471111, "small":272131, "deep":10102, "large":883901, "huge":528540, "purple":772529, "orange":590053, "soft":735741 },
            "spoon":{ "red":980353, "blue":988334, "green":996391, "black":196248, "white":554820, "magenta":964646, "big":629526, "small":560344, "deep":753880, "large":195107, "huge":445930, "purple":988212, "orange":634329, "soft":641271 },
            "fork":{ "red":790496, "blue":395728, "green":753461, "black":337613, "white":200118, "magenta":819560, "big":867341, "small":517021, "deep":719636, "large":431383, "huge":730552, "purple":85502, "orange":438928, "soft":342373 },
            "pot":{ "red":563960, "blue":545981, "green":156785, "black":147555, "white":890105, "magenta":599672, "big":847142, "small":594421, "deep":875120, "large":375680, "huge":154420, "purple":83545, "orange":361895, "soft":171195 },
            "cable":{ "red":993725, "blue":586815, "green":240964, "black":364895, "white":225527, "magenta":126548, "big":44410, "small":743602, "deep":396408, "large":128808, "huge":518583, "purple":323810, "orange":9142, "soft":429124 },
            "case":{ "red":669991, "blue":842447, "green":539304, "black":398496, "white":126331, "magenta":958885, "big":412445, "small":74386, "deep":643557, "large":931314, "huge":532467, "purple":748317, "orange":949346, "soft":515124 },
            "music":{ "red":244037, "blue":386027, "green":178696, "black":406578, "white":595579, "magenta":310726, "big":897285, "small":56596, "deep":414045, "large":232164, "huge":709682, "purple":182387, "orange":214471, "soft":88366 },
            "bike":{ "red":851072, "blue":971226, "green":827334, "black":498071, "white":915997, "magenta":700075, "big":446040, "small":673871, "deep":75995, "large":517420, "huge":168686, "purple":547335, "orange":471112, "soft":362411 },
            "hamburger":{ "red":370728, "blue":961220, "green":830790, "black":836621, "white":239179, "magenta":698505, "big":318389, "small":103789, "deep":196663, "large":528996, "huge":529823, "purple":505432, "orange":642060, "soft":170362 },
            "pizza":{ "red":771197, "blue":324162, "green":392334, "black":63912, "white":914058, "magenta":408172, "big":395447, "small":28360, "deep":965433, "large":94459, "huge":34879, "purple":477378, "orange":672110, "soft":746076 },
            "keys":{ "red":371387, "blue":325301, "green":779635, "black":353863, "white":143454, "magenta":103876, "big":558365, "small":707719, "deep":552822, "large":129091, "huge":450961, "purple":731926, "orange":977578, "soft":734815 }
        },
        "k":
            {"laptop":{ "red":268041, "blue":886766, "green":254721, "black":205152, "white":764771, "magenta":662291, "big":716652, "small":210171, "deep":380512, "large":655361, "huge":406608, "purple":974600, "orange":764282, "soft":187285 },
            "remote control":{ "red":994203, "blue":188222, "green":280212, "black":472511, "white":994183, "magenta":832460, "big":132375, "small":556433, "deep":710230, "large":291779, "huge":11998, "purple":589667, "orange":517704, "soft":381791 },
            "bowl":{ "red":478075, "blue":57784, "green":927731, "black":134537, "white":677583, "magenta":318805, "big":132256, "small":980201, "deep":361889, "large":341209, "huge":831975, "purple":954656, "orange":179040, "soft":337132 },
            "spoon":{ "red":311853, "blue":631434, "green":854446, "black":275949, "white":371216, "magenta":28025, "big":86722, "small":762688, "deep":782449, "large":865660, "huge":964604, "purple":189968, "orange":696513, "soft":401659 },
            "fork":{ "red":747211, "blue":730625, "green":127582, "black":609712, "white":517493, "magenta":586446, "big":707315, "small":933919, "deep":244568, "large":335777, "huge":589204, "purple":690519, "orange":610574, "soft":82669 },
            "pot":{ "red":618671, "blue":500212, "green":529483, "black":808032, "white":128982, "magenta":921329, "big":796557, "small":287960, "deep":245689, "large":421679, "huge":372609, "purple":499604, "orange":575853, "soft":735094 },
            "cable":{ "red":234006, "blue":658311, "green":830780, "black":311857, "white":685276, "magenta":342188, "big":376750, "small":390401, "deep":724846, "large":224068, "huge":656588, "purple":615577, "orange":517306, "soft":704544 },
            "case":{ "red":246705, "blue":391608, "green":478252, "black":846209, "white":171693, "magenta":236941, "big":624306, "small":190792, "deep":599273, "large":105509, "huge":366115, "purple":818242, "orange":984118, "soft":969279 },
            "music":{ "red":659061, "blue":106485, "green":803472, "black":622199, "white":353084, "magenta":719246, "big":502193, "small":525793, "deep":487303, "large":339299, "huge":951308, "purple":506491, "orange":49372, "soft":908082 },
            "bike":{ "red":41420, "blue":142854, "green":261511, "black":800344, "white":609134, "magenta":652807, "big":416599, "small":174274, "deep":703067, "large":908740, "huge":791142, "purple":769003, "orange":903766, "soft":619703 },
            "hamburger":{ "red":204189, "blue":942465, "green":448385, "black":20454, "white":617099, "magenta":21909, "big":347989, "small":405190, "deep":365640, "large":814552, "huge":929532, "purple":247775, "orange":779245, "soft":742732 },
            "pizza":{ "red":429412, "blue":447516, "green":380980, "black":574137, "white":851655, "magenta":523443, "big":626442, "small":447002, "deep":541742, "large":202007, "huge":66584, "purple":64351, "orange":42900, "soft":397017 },
            "keys":{ "red":142404, "blue":17606, "green":383931, "black":999387, "white":242230, "magenta":26547, "big":22530, "small":725230, "deep":854695, "large":226482, "huge":483674, "purple":639845, "orange":632132, "soft":636836 }
        }
    }

    items = {
        "laptop":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "remote control":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"}, 
        "bowl":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "spoon":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "fork":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "pot":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "cable":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "case":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "music":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "bike":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "hamburger":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "pizza":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"},
        "keys":{"red","blue","green","black","white","magenta","big","small","deep","large","huge","purple","orange","soft"}
        }
    catagories  = ["laptop", "remote control","bowl", "spoon", "fork","pot","keys"]
    agents_names = ['a','b','c','d','e','f','G','h','i','j','k']

    # python implementation of the algorithm.
    n_size.append(get_n_size(catagories, items, agents_names))
    data = fair_division_python.Data(catagories,agents_evaluation,items)
    start = time.perf_counter()
    allocation = fair_division_python.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    runntime.append(total_time)

    # cython (C generated python) implementation of the algorithm.
    start = time.perf_counter()
    allocation = fair_division_cython.ef1_algorithm(agents_names, data)
    end = time.perf_counter()
    total_time= round(end - start,3)
    improved_runntime.append(total_time)

    print(runntime)
    print(improved_runntime)
    print(n_size)

if __name__ == "__main__":
    import numpy as np
    
    evaluate_improvment_from_original()
    n_size = [12, 13, 74, 77, 116]
    runtime = np.array([111.1, 100, 200, 890, 1407.5]) 
    improved_runntime= np.array([0.0, 100, 200, 115, 1056.8]) 
    plot_time_graph(n_size, runtime, improved_runntime)
