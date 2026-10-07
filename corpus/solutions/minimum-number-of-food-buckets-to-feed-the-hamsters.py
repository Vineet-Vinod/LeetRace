class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        buckets = [False] * len(hamsters)
        count = 0
        for i, ch in enumerate(hamsters):
            if ch != "H" or (i > 0 and buckets[i - 1]):
                continue
            if i + 1 < len(hamsters) and hamsters[i + 1] == ".":
                buckets[i + 1] = True
            elif i > 0 and hamsters[i - 1] == ".":
                buckets[i - 1] = True
            else:
                return -1
            count += 1
        return count
