from typing import List
from functools import cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        @cache
        def sentences(i: int) -> List[str]:
            if i == len(s):
                return [""]
            ans = []
            for j in range(i + 1, min(len(s), i + 10) + 1):
                word = s[i:j]
                if word in words:
                    for tail in sentences(j):
                        ans.append(word + (" " + tail if tail else ""))
            return ans

        return sorted(sentences(0))
