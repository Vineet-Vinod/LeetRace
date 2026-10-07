class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children: list[list[int]] = [[] for _ in range(n)]
        for node in range(1, n):
            children[parents[node]].append(node)
        sizes = [1] * n
        order = [0]
        for node in order:
            order.extend(children[node])
        scores = [1] * n
        highest = 0
        for node in reversed(order):
            remaining = n - 1
            score = 1
            for child in children[node]:
                sizes[node] += sizes[child]
                score *= sizes[child]
                remaining -= sizes[child]
            if remaining:
                score *= remaining
            scores[node] = score
            highest = max(highest, score)
        return sum(score == highest for score in scores)
