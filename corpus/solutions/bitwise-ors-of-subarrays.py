class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ending: set[int] = set()
        answer: set[int] = set()
        for value in arr:
            ending = {value | prior for prior in ending} | {value}
            answer.update(ending)
        return len(answer)
