class Solution:
    def splitLoopedString(self, strs: list[str]) -> str:
        oriented = [max(value, value[::-1]) for value in strs]
        best = ""
        for index, value in enumerate(strs):
            middle = "".join(oriented[index + 1 :] + oriented[:index])
            for candidate in {value, value[::-1]}:
                for cut in range(len(candidate)):
                    best = max(best, candidate[cut:] + middle + candidate[:cut])
        return best
