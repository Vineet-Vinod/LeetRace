class Solution:
    def findReplaceString(
        self, s: str, indices: List[int], sources: List[str], targets: List[str]
    ) -> str:
        operations = sorted(zip(indices, sources, targets))
        pieces = []
        cursor = 0
        for index, source, target in operations:
            if index < cursor:
                continue
            pieces.append(s[cursor:index])
            if s[index : index + len(source)] == source:
                pieces.append(target)
                cursor = index + len(source)
            else:
                cursor = index
        pieces.append(s[cursor:])
        return "".join(pieces)
