class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word: str) -> bool:
            forward: dict[str, str] = {}
            reverse: dict[str, str] = {}
            for source, target in zip(pattern, word):
                if (
                    forward.get(source, target) != target
                    or reverse.get(target, source) != source
                ):
                    return False
                forward[source] = target
                reverse[target] = source
            return True

        return [word for word in words if matches(word)]
