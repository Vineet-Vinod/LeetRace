class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answers: list[list[int]] = []
        current: list[int] = []

        def search(start: int, remaining: int) -> None:
            if len(current) == k:
                if remaining == 0:
                    answers.append(current.copy())
                return
            slots = k - len(current)
            for value in range(start, 10):
                if value > remaining:
                    break
                if sum(range(value, value + slots)) > remaining:
                    break
                current.append(value)
                search(value + 1, remaining - value)
                current.pop()

        search(1, n)
        return answers
