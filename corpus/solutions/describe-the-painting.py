class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        events = {}
        for start, end, color in segments:
            events[start] = events.get(start, 0) + color
            events[end] = events.get(end, 0) - color
        answer = []
        running = 0
        previous = None
        for position in sorted(events):
            if previous is not None and previous < position and running:
                answer.append([previous, position, running])
            running += events[position]
            previous = position
        return answer
