class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required = [0] * 26
        for word in words2:
            counts = Counter(word)
            for index, char in enumerate(string.ascii_lowercase):
                required[index] = max(required[index], counts[char])
        answer = []
        for word in words1:
            counts = Counter(word)
            if all(
                counts[char] >= required[index]
                for index, char in enumerate(string.ascii_lowercase)
            ):
                answer.append(word)
        return answer
