from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        children = [{}]
        counts = [0]
        answer = 0
        for word in words:
            node = 0
            for a, b in zip(word, reversed(word)):
                pair = (a, b)
                if pair not in children[node]:
                    children[node][pair] = len(children)
                    children.append({})
                    counts.append(0)
                node = children[node][pair]
                answer += counts[node]
            counts[node] += 1
        return answer
