class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:
        order = list(windows)
        for window in queries:
            order.remove(window)
            order.insert(0, window)
        return order
