class Solution:
    def newInteger(self, n: int) -> int:
        answer, place = 0, 1
        while n:
            n, digit = divmod(n, 9)
            answer += digit * place
            place *= 10
        return answer
