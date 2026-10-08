class Solution:
    def findRLEArray(
        self, encoded1: List[List[int]], encoded2: List[List[int]]
    ) -> List[List[int]]:
        i = j = 0
        remaining1, remaining2 = encoded1[0][1], encoded2[0][1]
        result: list[list[int]] = []
        while i < len(encoded1) and j < len(encoded2):
            count = min(remaining1, remaining2)
            product = encoded1[i][0] * encoded2[j][0]
            if result and result[-1][0] == product:
                result[-1][1] += count
            else:
                result.append([product, count])
            remaining1 -= count
            remaining2 -= count
            if remaining1 == 0:
                i += 1
                if i < len(encoded1):
                    remaining1 = encoded1[i][1]
            if remaining2 == 0:
                j += 1
                if j < len(encoded2):
                    remaining2 = encoded2[j][1]
        return result
