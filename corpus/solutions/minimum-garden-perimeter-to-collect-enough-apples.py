class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        radius = 0
        while 2 * radius * (radius + 1) * (2 * radius + 1) < neededApples:
            radius += 1
        return 8 * radius
