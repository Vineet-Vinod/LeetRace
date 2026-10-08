class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        if max(map(len, words)) > len(result):
            return False
        leading = {w[0] for w in words + [result] if len(w) > 1}
        words = [w[::-1] for w in words]
        result = result[::-1]
        mapping: dict[str, int] = {}
        used: set[int] = set()

        def solve(column: int, row: int, total: int) -> bool:
            if column == len(result):
                return total == 0
            if row == len(words):
                digit = total % 10
                ch = result[column]
                if ch in mapping:
                    return mapping[ch] == digit and solve(column + 1, 0, total // 10)
                if digit in used or digit == 0 and ch in leading:
                    return False
                mapping[ch] = digit
                used.add(digit)
                found = solve(column + 1, 0, total // 10)
                del mapping[ch]
                used.remove(digit)
                return found
            if column >= len(words[row]):
                return solve(column, row + 1, total)
            ch = words[row][column]
            if ch in mapping:
                return solve(column, row + 1, total + mapping[ch])
            for digit in range(10):
                if digit in used or digit == 0 and ch in leading:
                    continue
                mapping[ch] = digit
                used.add(digit)
                found = solve(column, row + 1, total + digit)
                del mapping[ch]
                used.remove(digit)
                if found:
                    return True
            return False

        return solve(0, 0, 0)
