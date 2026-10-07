from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter

        width = len(words[0])
        need = Counter(words)
        answer = []
        for offset in range(width):
            left, count = offset, 0
            have: dict[str, int] = {}
            for right in range(offset, len(s) - width + 1, width):
                word = s[right : right + width]
                if word not in need:
                    have.clear()
                    count = 0
                    left = right + width
                    continue
                have[word] = have.get(word, 0) + 1
                count += 1
                while have[word] > need[word]:
                    old = s[left : left + width]
                    have[old] -= 1
                    count -= 1
                    left += width
                if count == len(words):
                    answer.append(left)
        return sorted(answer)
