class Solution:
    def addBoldTag(self, s: str, words: list[str]) -> str:
        bold = [False] * len(s)
        for word in words:
            start = s.find(word)
            while start != -1:
                for index in range(start, start + len(word)):
                    bold[index] = True
                start = s.find(word, start + 1)

        result: list[str] = []
        index = 0
        while index < len(s):
            if not bold[index]:
                result.append(s[index])
                index += 1
                continue
            end = index
            while end < len(s) and bold[end]:
                end += 1
            result.append("<b>" + s[index:end] + "</b>")
            index = end
        return "".join(result)
