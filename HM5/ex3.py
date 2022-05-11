import itertools
from typing import List, Tuple

subsequences= []
n = int(input())
for i in range(n):
    subsequences.append(input())

permutations =  list(itertools.permutations(subsequences)) ; min_length = 60

for permutation in permutations:
    sequence = permutation[0]
    for i in range(1, len(permutation)):
        j = 0
        while j < len(sequence):
            subsequence = permutation[i]
            if sequence.find(subsequence) != -1:
                break
            end_index = len(sequence) - j
            if sequence[j:] == subsequence[:end_index]:
                sequence += subsequence[end_index:]
            j += 1
        if j == len(sequence):
            sequence += subsequence
    min_length = min(min_length, len(sequence))
print(min_length)