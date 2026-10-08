class Solution:
    def stringCount(self, n: int) -> int:
        modulus = 1_000_000_007
        counts = [[[0] * 2 for _ in range(3)] for _ in range(2)]
        counts[0][0][0] = 1
        for _ in range(n):
            next_counts = [[[0] * 2 for _ in range(3)] for _ in range(2)]
            for has_l in range(2):
                for e_count in range(3):
                    for has_t in range(2):
                        ways = counts[has_l][e_count][has_t]
                        if ways:
                            next_counts[1][e_count][has_t] += ways
                            next_counts[has_l][min(2, e_count + 1)][has_t] += ways
                            next_counts[has_l][e_count][1] += ways
                            next_counts[has_l][e_count][has_t] += 23 * ways
            for has_l in range(2):
                for e_count in range(3):
                    for has_t in range(2):
                        next_counts[has_l][e_count][has_t] %= modulus
            counts = next_counts
        return counts[1][2][1]
