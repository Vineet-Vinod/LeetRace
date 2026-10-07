class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        # Range-add and prefix-sum Fenwick trees track distinct counts by start index.
        first = [0] * (n + 2)
        second = [0] * (n + 2)

        def add(tree: list[int], i: int, value: int) -> None:
            while i <= n + 1:
                tree[i] += value
                i += i & -i

        def prefix(i: int) -> int:
            a = b = 0
            j = i
            while j:
                a += first[j]
                b += second[j]
                j -= j & -j
            return a * i - b

        last: dict[int, int] = {}
        squares = answer = 0
        for right, value in enumerate(nums, 1):
            left = last.get(value, 0) + 1
            old = prefix(right) - prefix(left - 1)
            squares += 2 * old + right - left + 1
            add(first, left, 1)
            add(first, right + 1, -1)
            add(second, left, left - 1)
            add(second, right + 1, -right)
            last[value] = right
            answer = (answer + squares) % 1000000007
        return answer
