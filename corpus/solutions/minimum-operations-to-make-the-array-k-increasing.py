from typing import List
from bisect import bisect_right


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        answer = 0
        for start in range(k):
            tails = []
            count = 0
            for i in range(start, len(arr), k):
                pos = bisect_right(tails, arr[i])
                if pos == len(tails):
                    tails.append(arr[i])
                else:
                    tails[pos] = arr[i]
                count += 1
            answer += count - len(tails)
        return answer
