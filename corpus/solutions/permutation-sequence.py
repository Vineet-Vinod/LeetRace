from math import factorial


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n + 1)]
        k -= 1
        answer = []
        while digits:
            block = factorial(len(digits) - 1)
            index, k = divmod(k, block)
            answer.append(digits.pop(index))
        return "".join(answer)
