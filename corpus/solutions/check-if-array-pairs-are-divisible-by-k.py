class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = Counter(value % k for value in arr)
        if counts[0] % 2:
            return False
        for remainder in range(1, k):
            if remainder == k - remainder:
                if counts[remainder] % 2:
                    return False
            elif counts[remainder] != counts[k - remainder]:
                return False
        return True
