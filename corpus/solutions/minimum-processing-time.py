class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        starts = sorted(processorTime)
        jobs = sorted(tasks, reverse=True)
        return max(starts[i] + jobs[4 * i] for i in range(len(starts)))
