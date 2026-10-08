class Solution:
    def minimumCosts(
        self, regular: List[int], express: List[int], expressCost: int
    ) -> List[int]:
        r, e = 0, expressCost
        answer = []
        for a, b in zip(regular, express):
            r, e = min(r, e) + a, min(e, r + expressCost) + b
            answer.append(min(r, e))
        return answer
