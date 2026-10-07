class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        @lru_cache(None)
        def can_finish(left_a: int, left_b: int, last: str, run: int) -> bool:
            if left_a == 0 and left_b == 0:
                return True
            if (
                left_a
                and not (last == "a" and run == 2)
                and can_finish(left_a - 1, left_b, "a", run + 1 if last == "a" else 1)
            ):
                return True
            if (
                left_b
                and not (last == "b" and run == 2)
                and can_finish(left_a, left_b - 1, "b", run + 1 if last == "b" else 1)
            ):
                return True
            return False

        result = []
        left_a, left_b = a, b
        last, run = "", 0
        while left_a or left_b:
            if (
                left_a
                and not (last == "a" and run == 2)
                and can_finish(left_a - 1, left_b, "a", run + 1 if last == "a" else 1)
            ):
                result.append("a")
                left_a -= 1
                run = run + 1 if last == "a" else 1
                last = "a"
            else:
                result.append("b")
                left_b -= 1
                run = run + 1 if last == "b" else 1
                last = "b"
        return "".join(result)
