class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star = -1
        consumed = 0
        while i < len(s):
            if j < len(p) and p[j] in (s[i], "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                star = j
                consumed = i
                j += 1
            elif star >= 0:
                consumed += 1
                i = consumed
                j = star + 1
            else:
                return False
        return all(char == "*" for char in p[j:])
