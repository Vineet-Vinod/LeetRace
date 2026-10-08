from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        chars = list(target)
        erased = 0
        reverse = []
        while erased < len(chars):
            for start in range(len(chars) - len(stamp) + 1):
                window = chars[start : start + len(stamp)]
                if all(a == "?" or a == b for a, b in zip(window, stamp)) and any(
                    a != "?" for a in window
                ):
                    erased += sum(a != "?" for a in window)
                    chars[start : start + len(stamp)] = ["?"] * len(stamp)
                    reverse.append(start)
                    break
            else:
                return []
        return reverse[::-1]
