class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        current = mass
        for asteroid in sorted(asteroids):
            if current < asteroid:
                return False
            current += asteroid
        return True
