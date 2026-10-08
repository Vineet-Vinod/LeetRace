class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result: list[str] = []
        for value in range(1, n + 1):
            word = ("Fizz" if value % 3 == 0 else "") + (
                "Buzz" if value % 5 == 0 else ""
            )
            result.append(word or str(value))
        return result
