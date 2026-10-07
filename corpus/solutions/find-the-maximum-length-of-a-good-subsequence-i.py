class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        best_by_budget = [0] * (k + 1)
        ending: Dict[int, List[int]] = {}
        for value in nums:
            previous = ending.get(value, [0] * (k + 1))
            global_before = best_by_budget.copy()
            updated = previous.copy()
            for budget in range(k + 1):
                updated[budget] = max(updated[budget], previous[budget] + 1)
                if budget > 0:
                    updated[budget] = max(
                        updated[budget], global_before[budget - 1] + 1
                    )
            ending[value] = updated
            for budget in range(k + 1):
                best_by_budget[budget] = max(best_by_budget[budget], updated[budget])
        return best_by_budget[k]
