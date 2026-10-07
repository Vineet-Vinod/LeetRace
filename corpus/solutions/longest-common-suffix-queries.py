class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        children: list[dict[str, int]] = [{}]
        best = [-1]
        for i, word in enumerate(wordsContainer):
            node = 0
            for char in [""] + list(reversed(word)):
                if char:
                    if char not in children[node]:
                        children[node][char] = len(children)
                        children.append({})
                        best.append(-1)
                    node = children[node][char]
                if best[node] == -1 or (len(word), i) < (
                    len(wordsContainer[best[node]]),
                    best[node],
                ):
                    best[node] = i
        answer = []
        for word in wordsQuery:
            node = 0
            for char in reversed(word):
                if char not in children[node]:
                    break
                node = children[node][char]
            answer.append(best[node])
        return answer
