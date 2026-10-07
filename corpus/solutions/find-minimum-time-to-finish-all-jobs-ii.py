class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort(reverse=True)
        workers.sort(reverse=True)
        days = 0
        for job, worker in zip(jobs, workers):
            days = max(days, (job + worker - 1) // worker)
        return days
