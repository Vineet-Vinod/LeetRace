from bisect import bisect_right
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        tails = []
        answer = []
        for height in obstacles:
            i = bisect_right(tails, height)
            if i == len(tails):
                tails.append(height)
            else:
                tails[i] = height
            answer.append(i + 1)
        return answer
