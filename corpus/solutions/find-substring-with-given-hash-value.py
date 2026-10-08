class Solution:
    def subStrHash(
        self, s: str, power: int, modulo: int, k: int, hashValue: int
    ) -> str:
        import builtins

        value = 0
        answer = 0
        factor = builtins.pow(power, k, modulo)
        for i in range(len(s) - 1, -1, -1):
            value = (value * power + ord(s[i]) - 96) % modulo
            if i + k < len(s):
                value = (value - (ord(s[i + k]) - 96) * factor) % modulo
            if i + k <= len(s) and value == hashValue:
                answer = i
        return s[answer : answer + k]
