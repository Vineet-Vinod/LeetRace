class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = flowerbed[:]
        count = 0
        for i, value in enumerate(planted):
            if (
                value == 0
                and (i == 0 or planted[i - 1] == 0)
                and (i + 1 == len(planted) or planted[i + 1] == 0)
            ):
                planted[i] = 1
                count += 1
        return count >= n
