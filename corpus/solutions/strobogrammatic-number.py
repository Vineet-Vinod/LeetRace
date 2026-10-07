class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotate = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        return all(
            char in rotate and rotate[char] == num[-1 - i] for i, char in enumerate(num)
        )
