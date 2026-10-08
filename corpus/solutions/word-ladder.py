from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict, deque

        words = set(wordList)
        if endWord not in words:
            return 0
        buckets = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                buckets[word[:i] + "*" + word[i + 1 :]].append(word)
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                for neighbor in buckets.pop(pattern, []):
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, distance + 1))
        return 0
