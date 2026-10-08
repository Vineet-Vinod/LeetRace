class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        values = dict(knowledge)
        result: List[str] = []
        index = 0
        while index < len(s):
            if s[index] != "(":
                result.append(s[index])
                index += 1
                continue
            end = s.index(")", index)
            result.append(values.get(s[index + 1 : end], "?"))
            index = end + 1
        return "".join(result)
