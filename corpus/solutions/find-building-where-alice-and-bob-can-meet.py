class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        import heapq

        pending = [[] for _ in heights]
        answer = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                answer[i] = b
            else:
                pending[b].append((heights[a], i))
        heap = []
        for j, height in enumerate(heights):
            while heap and heap[0][0] < height:
                _, i = heapq.heappop(heap)
                answer[i] = j
            for item in pending[j]:
                heapq.heappush(heap, item)
        return answer
