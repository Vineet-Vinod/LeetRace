from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        answer: list[str] = []

        def search(index: int, expression: str, total: int, last: int) -> None:
            if index == len(num):
                if total == target:
                    answer.append(expression)
                return
            for end in range(index + 1, len(num) + 1):
                if end > index + 1 and num[index] == "0":
                    break
                text = num[index:end]
                value = int(text)
                if index == 0:
                    search(end, text, value, value)
                else:
                    search(end, expression + "+" + text, total + value, value)
                    search(end, expression + "-" + text, total - value, -value)
                    search(
                        end,
                        expression + "*" + text,
                        total - last + last * value,
                        last * value,
                    )

        search(0, "", 0, 0)
        return sorted(answer)
