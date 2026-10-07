class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i = len(arr1) - 1
        j = len(arr2) - 1
        carry = 0
        result: list[int] = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += arr1[i]
                i -= 1
            if j >= 0:
                total += arr2[j]
                j -= 1
            bit = total & 1
            result.append(bit)
            carry = (total - bit) // -2
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result[::-1]
