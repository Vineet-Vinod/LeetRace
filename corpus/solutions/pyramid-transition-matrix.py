class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        choices: dict[str, list[str]] = {}
        for pattern in allowed:
            choices.setdefault(pattern[:2], []).append(pattern[2])

        @cache
        def can_build(row: str) -> bool:
            if len(row) == 1:
                return True

            def build_next(index: int, next_row: str) -> bool:
                if index == len(row) - 1:
                    return can_build(next_row)
                for top in choices.get(row[index : index + 2], []):
                    if build_next(index + 1, next_row + top):
                        return True
                return False

            return build_next(0, "")

        return can_build(bottom)
