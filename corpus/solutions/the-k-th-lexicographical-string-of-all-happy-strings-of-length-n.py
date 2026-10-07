class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n - 1)):
            return ""
        result: list[str] = []
        previous = ""
        for position in range(n):
            block = 1 << (n - position - 1)
            for char in "abc":
                if char == previous:
                    continue
                if k > block:
                    k -= block
                else:
                    result.append(char)
                    previous = char
                    break
        return "".join(result)
