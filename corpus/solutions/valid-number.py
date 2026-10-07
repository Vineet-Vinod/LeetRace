import re


class Solution:
    def isNumber(self, s: str) -> bool:
        return (
            re.fullmatch(
                r"[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?", s
            )
            is not None
        )
