class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        target = list(num)
        for _ in range(k):
            i = len(target) - 2
            while target[i] >= target[i + 1]:
                i -= 1
            j = len(target) - 1
            while target[j] <= target[i]:
                j -= 1
            target[i], target[j] = target[j], target[i]
            target[i + 1 :] = reversed(target[i + 1 :])
        source = list(num)
        swaps = 0
        for i, wanted in enumerate(target):
            j = i
            while source[j] != wanted:
                j += 1
            while j > i:
                source[j], source[j - 1] = source[j - 1], source[j]
                swaps += 1
                j -= 1
        return swaps
