class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        cycle_length = gcd(len(arr), k)
        operations = 0
        for start in range(cycle_length):
            cycle = []
            index = start
            while True:
                cycle.append(arr[index])
                index = (index + k) % len(arr)
                if index == start:
                    break
            cycle.sort()
            median = cycle[len(cycle) // 2]
            operations += sum(abs(value - median) for value in cycle)
        return operations
