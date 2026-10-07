class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        from collections import Counter

        counts = Counter(s)
        alphabet = sorted((char for char in counts if counts[char] >= k), reverse=True)

        def valid(word: str) -> bool:
            index = repeats = 0
            for char in s:
                if char == word[index]:
                    index += 1
                    if index == len(word):
                        repeats += 1
                        index = 0
                        if repeats == k:
                            return True
            return False

        level = [""]
        answer = ""
        while level:
            following = []
            for prefix in level:
                for char in alphabet:
                    if prefix.count(char) + 1 > counts[char] // k:
                        continue
                    word = prefix + char
                    if valid(word):
                        following.append(word)
            if following:
                answer = max(following)
            level = following
        return answer
