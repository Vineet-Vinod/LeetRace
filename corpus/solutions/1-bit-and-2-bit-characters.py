class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0
        while index < len(bits) - 1:
            index += 2 if bits[index] == 1 else 1
        return index == len(bits) - 1
