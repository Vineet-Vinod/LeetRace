class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            value = 0
            for k in range(i, len(arr)):
                value ^= arr[k]
                if value == 0:
                    count += k - i
        return count
