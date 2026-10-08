class Solution:
    def largestGoodInteger(self, num: str) -> str:
        found = [
            num[i : i + 3]
            for i in range(len(num) - 2)
            if num[i] == num[i + 1] == num[i + 2]
        ]
        return max(found, default="")
