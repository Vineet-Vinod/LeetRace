class Solution:
    def areSentencesSimilarTwo(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        parent = {}

        def find(x: str) -> str:
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for a, b in similarPairs:
            parent[find(a)] = find(b)
        return all(
            a == b or (a in parent and b in parent and find(a) == find(b))
            for a, b in zip(sentence1, sentence2)
        )
