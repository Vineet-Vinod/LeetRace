class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        children = [{}]
        counts = [0]
        for word in words:
            node = 0
            for c in word:
                if c not in children[node]:
                    children[node][c] = len(children)
                    children.append({})
                    counts.append(0)
                node = children[node][c]
                counts[node] += 1
        answer = []
        for word in words:
            node = 0
            total = 0
            for c in word:
                node = children[node][c]
                total += counts[node]
            answer.append(total)
        return answer
