class Solution:
    def minFlips(self, target: str) -> int:
        previous = "0"
        answer = 0
        for bit in target:
            if bit != previous:
                answer += 1
                previous = bit
        return answer
