from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        answer = [-1.0] * len(cars)
        stack: list[int] = []
        for i in range(len(cars) - 1, -1, -1):
            position, speed = cars[i]
            while stack:
                j = stack[-1]
                if speed <= cars[j][1]:
                    stack.pop()
                    continue
                time = (cars[j][0] - position) / (speed - cars[j][1])
                if answer[j] < 0 or time <= answer[j]:
                    answer[i] = time
                    break
                stack.pop()
            stack.append(i)
        return answer
