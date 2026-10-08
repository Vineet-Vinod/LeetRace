class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 1000000007
        end0 = [[0] * (one + 1) for _ in range(zero + 1)]
        end1 = [[0] * (one + 1) for _ in range(zero + 1)]
        for i in range(1, min(zero, limit) + 1):
            end0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            end1[0][j] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                a = end0[i - 1][j] + end1[i - 1][j]
                if i > limit:
                    a -= end1[i - limit - 1][j]
                end0[i][j] = a % mod
                b = end0[i][j - 1] + end1[i][j - 1]
                if j > limit:
                    b -= end0[i][j - limit - 1]
                end1[i][j] = b % mod
        return (end0[zero][one] + end1[zero][one]) % mod
