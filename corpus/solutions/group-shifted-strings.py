class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups: Dict[Tuple[int, ...], List[str]] = {}
        for value in strings:
            key = tuple(
                (ord(value[index]) - ord(value[0])) % 26 for index in range(len(value))
            )
            groups.setdefault(key, []).append(value)
        result = [sorted(group) for group in groups.values()]
        return sorted(result)
