class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []
        path = []

        def search(start: int, remaining: int) -> None:
            if remaining == 0:
                answer.append(path.copy())
                return
            for index in range(start, len(candidates)):
                value = candidates[index]
                if index > start and value == candidates[index - 1]:
                    continue
                if value > remaining:
                    break
                path.append(value)
                search(index + 1, remaining - value)
                path.pop()

        search(0, target)
        return answer
