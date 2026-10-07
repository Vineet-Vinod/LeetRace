class Solution:
    def sumGame(self, num: str) -> bool:
        middle = len(num) // 2
        left_sum = sum(int(char) for char in num[:middle] if char != "?")
        right_sum = sum(int(char) for char in num[middle:] if char != "?")
        question_difference = num[:middle].count("?") - num[middle:].count("?")
        return (
            question_difference % 2 != 0
            or left_sum - right_sum != -9 * question_difference // 2
        )
