class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        attainable = [False, False, False]
        for triplet in triplets:
            if all(value <= limit for value, limit in zip(triplet, target)):
                for i in range(3):
                    if triplet[i] == target[i]:
                        attainable[i] = True
        return all(attainable)
