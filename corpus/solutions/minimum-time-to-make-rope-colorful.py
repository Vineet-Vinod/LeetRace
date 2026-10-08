class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        index = 0
        while index < len(colors):
            end = index + 1
            group_sum = neededTime[index]
            largest = neededTime[index]
            while end < len(colors) and colors[end] == colors[index]:
                group_sum += neededTime[end]
                largest = max(largest, neededTime[end])
                end += 1
            total += group_sum - largest
            index = end
        return total
