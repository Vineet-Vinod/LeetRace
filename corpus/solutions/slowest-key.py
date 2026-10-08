class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest = -1
        answer = ""
        previous = 0
        for duration, key in zip(releaseTimes, keysPressed):
            elapsed = duration - previous
            previous = duration
            if elapsed > longest or elapsed == longest and key > answer:
                longest = elapsed
                answer = key
        return answer
