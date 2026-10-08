class Solution:
    def minimumTimeRequired(self, jobs: list[int], k: int) -> int:
        jobs = sorted(jobs, reverse=True)
        low, high = max(max(jobs), (sum(jobs) + k - 1) // k), sum(jobs)

        def feasible(limit: int) -> bool:
            loads = [0] * k

            def assign(i: int) -> bool:
                if i == len(jobs):
                    return True
                seen = set()
                for worker in range(k):
                    current = loads[worker]
                    if current in seen or current + jobs[i] > limit:
                        continue
                    seen.add(current)
                    loads[worker] += jobs[i]
                    if assign(i + 1):
                        return True
                    loads[worker] -= jobs[i]
                    if current == 0:
                        break
                return False

            return assign(0)

        while low < high:
            mid = (low + high) // 2
            if feasible(mid):
                high = mid
            else:
                low = mid + 1
        return low
