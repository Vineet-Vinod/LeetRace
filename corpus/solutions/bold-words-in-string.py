class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        bold = [False] * len(s)
        for word in words:
            start = 0
            while True:
                start = s.find(word, start)
                if start == -1:
                    break
                for index in range(start, start + len(word)):
                    bold[index] = True
                start += 1
        parts: list[str] = []
        index = 0
        while index < len(s):
            if not bold[index]:
                parts.append(s[index])
                index += 1
                continue
            end = index
            while end < len(s) and bold[end]:
                end += 1
            parts.extend(["<b>", s[index:end], "</b>"])
            index = end
        return "".join(parts)
