class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        used = 0
        current = 0
        index = 0
        while current < time:
            farthest = current
            while index < len(clips) and clips[index][0] <= current:
                farthest = max(farthest, clips[index][1])
                index += 1
            if farthest == current:
                return -1
            used += 1
            current = farthest
        return used
