from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        seats = row.copy()
        positions = [0] * len(row)
        for i, person in enumerate(seats):
            positions[person] = i
        answer = 0
        for i in range(0, len(seats), 2):
            partner = seats[i] ^ 1
            if seats[i + 1] != partner:
                j = positions[partner]
                other = seats[i + 1]
                seats[i + 1], seats[j] = partner, other
                positions[partner], positions[other] = i + 1, j
                answer += 1
        return answer
