class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ordered = sorted(candidates)
        combinations: List[List[int]] = []
        current: List[int] = []

        def search(start: int, remaining: int) -> None:
            if remaining == 0:
                combinations.append(current.copy())
                return
            for index in range(start, len(ordered)):
                value = ordered[index]
                if value > remaining:
                    break
                current.append(value)
                search(index, remaining - value)
                current.pop()

        search(0, target)
        return sorted(combinations)
