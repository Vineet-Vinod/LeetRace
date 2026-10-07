class Solution:
    def primePalindrome(self, n: int) -> int:
        def prime(x: int) -> bool:
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            d = 3
            while d * d <= x:
                if x % d == 0:
                    return False
                d += 2
            return True

        if 8 <= n <= 11:
            return 11
        for length in range(len(str(n)), 9):
            half = (length + 1) // 2
            for prefix in range(10 ** (half - 1), 10**half):
                text = str(prefix)
                pal = (
                    int(text + text[-(length % 2 + 1) :: -1])
                    if length % 2 == 0
                    else int(text + text[-2::-1])
                )
                if pal >= n and prime(pal):
                    return pal
        return 100030001
