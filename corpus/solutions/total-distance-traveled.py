class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        while mainTank >= 5:
            mainTank -= 5
            distance += 50
            if additionalTank:
                mainTank += 1
                additionalTank -= 1
        return distance + mainTank * 10
