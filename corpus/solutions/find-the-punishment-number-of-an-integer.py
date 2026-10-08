class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(text: str, target: int, index: int = 0) -> bool:
            if index == len(text):
                return target == 0
            value = 0
            for end in range(index, len(text)):
                value = value * 10 + int(text[end])
                if value > target:
                    break
                if can_partition(text, target - value, end + 1):
                    return True
            return False

        return sum(
            value * value
            for value in range(1, n + 1)
            if can_partition(str(value * value), value)
        )
