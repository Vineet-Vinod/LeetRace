class Solution:
    def getPermutationIndex(self, perm: List[int]) -> int:
        n = len(perm)
        mod = 10**9 + 7
        factorial = [1] * (n + 1)
        for value in range(1, n + 1):
            factorial[value] = factorial[value - 1] * value % mod
        tree = [0] * (n + 1)

        def add(index: int) -> None:
            while index <= n:
                tree[index] += 1
                index += index & -index

        def prefix(index: int) -> int:
            count = 0
            while index:
                count += tree[index]
                index -= index & -index
            return count

        for value in range(1, n + 1):
            add(value)
        rank = 0
        for index, value in enumerate(perm):
            smaller_unused = prefix(value - 1)
            rank = (rank + smaller_unused * factorial[n - index - 1]) % mod
            position = value
            while position <= n:
                tree[position] -= 1
                position += position & -position
        return rank
