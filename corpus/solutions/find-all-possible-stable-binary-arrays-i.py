class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        modulus = 1_000_000_007
        ending_zero = [[0] * (one + 1) for _ in range(zero + 1)]
        ending_one = [[0] * (one + 1) for _ in range(zero + 1)]
        for zeros in range(zero + 1):
            for ones in range(one + 1):
                if zeros <= limit and ones == 0 and zeros:
                    ending_zero[zeros][ones] = 1
                if ones <= limit and zeros == 0 and ones:
                    ending_one[zeros][ones] = 1
                for length in range(1, min(limit, zeros) + 1):
                    ending_zero[zeros][ones] += ending_one[zeros - length][ones]
                for length in range(1, min(limit, ones) + 1):
                    ending_one[zeros][ones] += ending_zero[zeros][ones - length]
                ending_zero[zeros][ones] %= modulus
                ending_one[zeros][ones] %= modulus
        return (ending_zero[zero][one] + ending_one[zero][one]) % modulus
