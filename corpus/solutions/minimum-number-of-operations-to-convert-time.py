class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def minutes(value):
            hours, mins = map(int, value.split(":"))
            return 60 * hours + mins

        difference = minutes(correct) - minutes(current)
        operations = 0
        for step in (60, 15, 5, 1):
            operations += difference // step
            difference %= step
        return operations
