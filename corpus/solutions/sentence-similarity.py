class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        pairs = {frozenset(pair) for pair in similarPairs}
        return all(
            first == second or frozenset((first, second)) in pairs
            for first, second in zip(sentence1, sentence2)
        )
