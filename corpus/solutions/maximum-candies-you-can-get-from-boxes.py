from typing import List


class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        owned = set(initialBoxes)
        opened = set()
        unlocked = {i for i, s in enumerate(status) if s}
        ready = list(owned & unlocked)
        answer = 0
        while ready:
            box = ready.pop()
            if box in opened or box not in owned or box not in unlocked:
                continue
            opened.add(box)
            answer += candies[box]
            for key in keys[box]:
                unlocked.add(key)
                if key in owned:
                    ready.append(key)
            for child in containedBoxes[box]:
                owned.add(child)
                if child in unlocked:
                    ready.append(child)
        return answer
