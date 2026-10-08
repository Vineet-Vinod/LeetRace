class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            identifier, content = log.split(" ", 1)
            (digits if content[0].isdigit() else letters).append(
                (identifier, content, log)
            )
        letters.sort(key=lambda item: (item[1], item[0]))
        return [item[2] for item in letters] + [
            log for log in logs if log.split(" ", 1)[1][0].isdigit()
        ]
