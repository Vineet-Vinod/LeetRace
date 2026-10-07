class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        answer = []
        depth = 0
        for char in seq:
            if char == "(":
                answer.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                answer.append(depth % 2)
        return answer
