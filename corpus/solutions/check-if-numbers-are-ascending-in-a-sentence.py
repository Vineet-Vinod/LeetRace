class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        previous = 0
        for token in s.split():
            if token.isdigit():
                value = int(token)
                if value <= previous:
                    return False
                previous = value
        return True
