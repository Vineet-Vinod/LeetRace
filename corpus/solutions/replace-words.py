class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        roots = set(dictionary)
        replaced = []
        for word in sentence.split():
            root = next(
                (
                    word[:length]
                    for length in range(1, len(word) + 1)
                    if word[:length] in roots
                ),
                word,
            )
            replaced.append(root)
        return " ".join(replaced)
