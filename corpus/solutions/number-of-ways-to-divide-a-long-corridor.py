class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = [i for i, ch in enumerate(corridor) if ch == "S"]
        if not seats or len(seats) % 2:
            return 0
        answer = 1
        for i in range(2, len(seats), 2):
            answer = answer * (seats[i] - seats[i - 1]) % 1000000007
        return answer
