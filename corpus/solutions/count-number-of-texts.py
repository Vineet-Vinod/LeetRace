class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        modulo = 10**9 + 7
        ways = [0] * (len(pressedKeys) + 1)
        ways[0] = 1
        for end in range(1, len(pressedKeys) + 1):
            maximum = 4 if pressedKeys[end - 1] in "79" else 3
            for length in range(1, maximum + 1):
                start = end - length
                if start < 0 or pressedKeys[start] != pressedKeys[end - 1]:
                    break
                ways[end] = (ways[end] + ways[start]) % modulo
        return ways[-1]
