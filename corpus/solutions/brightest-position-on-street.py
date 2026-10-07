class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = []
        for position, radius in lights:
            events.append((position - radius, 1))
            events.append((position + radius + 1, -1))
        events.sort()
        brightness = best = 0
        answer = 0
        for position, change in events:
            brightness += change
            if brightness > best:
                best = brightness
                answer = position
        return answer
