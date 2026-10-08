class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def gain(passed: int, total: int) -> float:
            return (passed + 1) / (total + 1) - passed / total

        heap = [(-gain(passed, total), passed, total) for passed, total in classes]
        heapify(heap)
        for _ in range(extraStudents):
            _, passed, total = heappop(heap)
            passed += 1
            total += 1
            heappush(heap, (-gain(passed, total), passed, total))
        return sum(passed / total for _, passed, total in heap) / len(classes)
