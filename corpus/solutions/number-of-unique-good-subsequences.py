class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        zero, one = 0, 0
        for char in binary:
            if char == "0":
                zero = (zero + one) % (10**9 + 7)
            else:
                one = (zero + one + 1) % (10**9 + 7)
        return (zero + one + int("0" in binary)) % (10**9 + 7)
