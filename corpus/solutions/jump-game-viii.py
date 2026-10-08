class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        size = len(nums)
        edges: List[List[int]] = [[] for _ in nums]
        stack: List[int] = []
        for index in range(size):
            while stack and nums[stack[-1]] <= nums[index]:
                edges[stack.pop()].append(index)
            stack.append(index)
        stack.clear()
        for index in range(size):
            while stack and nums[stack[-1]] > nums[index]:
                edges[stack.pop()].append(index)
            stack.append(index)
        distances = [float("inf")] * size
        distances[0] = 0
        heap: List[Tuple[int, int]] = [(0, 0)]
        while heap:
            distance, index = heappop(heap)
            if distance != distances[index]:
                continue
            if index == size - 1:
                return distance
            for following in edges[index]:
                candidate = distance + costs[following]
                if candidate < distances[following]:
                    distances[following] = candidate
                    heappush(heap, (candidate, following))
        return -1
