class Solution:
    def countOrders(self, n: int) -> int:
        answer = 1
        for i in range(1, n + 1):
            answer = answer * i * (2 * i - 1) % 1000000007
        return answer
