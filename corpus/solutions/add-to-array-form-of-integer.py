class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result: list[int] = []
        carry = k
        index = len(num) - 1
        while index >= 0 or carry:
            digit = carry % 10
            carry //= 10
            if index >= 0:
                digit += num[index]
                index -= 1
            result.append(digit % 10)
            carry += digit // 10
        while index >= 0:
            result.append(num[index])
            index -= 1
        return result[::-1]
