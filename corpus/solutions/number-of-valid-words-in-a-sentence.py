class Solution:
    def countValidWords(self, sentence: str) -> int:
        count = 0
        for token in sentence.split():
            hyphens = token.count("-")
            punctuation = [i for i, char in enumerate(token) if char in "!.,"]
            if (
                any(char.isdigit() for char in token)
                or hyphens > 1
                or len(punctuation) > 1
            ):
                continue
            if punctuation and punctuation[0] != len(token) - 1:
                continue
            if hyphens:
                i = token.index("-")
                if (
                    i == 0
                    or i == len(token) - 1
                    or not token[i - 1].islower()
                    or not token[i + 1].islower()
                ):
                    continue
            if any(
                char in "!.," for i, char in enumerate(token) if i not in punctuation
            ):
                continue
            count += 1
        return count
