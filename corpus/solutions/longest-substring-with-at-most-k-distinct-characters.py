class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        counts: Dict[str, int] = defaultdict(int)
        left = answer = 0
        for right, char in enumerate(s):
            counts[char] += 1
            while len(counts) > k:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
            answer = max(answer, right - left + 1)
        return answer
