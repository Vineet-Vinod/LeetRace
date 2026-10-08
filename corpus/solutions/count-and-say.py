class Solution:
    def countAndSay(self, n: int) -> str:
        term = "1"
        for _ in range(n - 1):
            parts: List[str] = []
            index = 0
            while index < len(term):
                end = index + 1
                while end < len(term) and term[end] == term[index]:
                    end += 1
                parts.append(str(end - index))
                parts.append(term[index])
                index = end
            term = "".join(parts)
        return term
