class Solution:
    def decodeString(self, s: str) -> str:
        counts = []
        prefixes = []
        current = []
        index = 0
        while index < len(s):
            if s[index].isdigit():
                multiplier = 0
                while index < len(s) and s[index].isdigit():
                    multiplier = multiplier * 10 + int(s[index])
                    index += 1
                counts.append(multiplier)
            elif s[index] == "[":
                prefixes.append("".join(current))
                current = []
                index += 1
            elif s[index] == "]":
                current = [prefixes.pop() + "".join(current) * counts.pop()]
                index += 1
            else:
                current.append(s[index])
                index += 1
        return "".join(current)
