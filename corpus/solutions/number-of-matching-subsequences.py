class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting: dict[str, list[tuple[str, int]]] = defaultdict(list)
        answer = 0
        for word in words:
            if not word:
                answer += 1
            else:
                waiting[word[0]].append((word, 0))
        for char in s:
            current = waiting.pop(char, [])
            for word, index in current:
                index += 1
                if index == len(word):
                    answer += 1
                else:
                    waiting[word[index]].append((word, index))
        return answer
