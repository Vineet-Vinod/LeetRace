class Solution:
    def getWordsInLongestSubsequence(
        self, words: List[str], groups: List[int]
    ) -> List[str]:
        size = len(words)
        lengths = [1] * size
        parent = [-1] * size
        for end in range(size):
            for start in range(end):
                if groups[start] == groups[end] or len(words[start]) != len(words[end]):
                    continue
                if sum(a != b for a, b in zip(words[start], words[end])) != 1:
                    continue
                if lengths[start] + 1 > lengths[end]:
                    lengths[end] = lengths[start] + 1
                    parent[end] = start
        endpoint = max(range(size), key=lambda index: (lengths[index], -index))
        indices = []
        while endpoint != -1:
            indices.append(endpoint)
            endpoint = parent[endpoint]
        indices.reverse()
        return [words[index] for index in indices]
