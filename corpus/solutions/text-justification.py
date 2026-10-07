from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        i = 0
        while i < len(words):
            j, letters = i, 0
            while j < len(words) and letters + len(words[j]) + j - i <= maxWidth:
                letters += len(words[j])
                j += 1
            if j == len(words) or j - i == 1:
                line = " ".join(words[i:j]).ljust(maxWidth)
            else:
                spaces, extra = divmod(maxWidth - letters, j - i - 1)
                line = words[i]
                for offset in range(j - i - 1):
                    line += " " * (spaces + (offset < extra)) + words[i + offset + 1]
            answer.append(line)
            i = j
        return answer
