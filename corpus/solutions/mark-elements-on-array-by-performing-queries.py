class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap = [(value, index) for index, value in enumerate(nums)]
        heapify(heap)
        marked = [False] * len(nums)
        total = sum(nums)
        answer: list[int] = []
        for index, count in queries:
            if not marked[index]:
                marked[index] = True
                total -= nums[index]
            while count and heap:
                value, next_index = heappop(heap)
                if marked[next_index]:
                    continue
                marked[next_index] = True
                total -= value
                count -= 1
            answer.append(total)
        return answer
