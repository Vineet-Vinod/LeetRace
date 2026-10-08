class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7
        previous = {}
        answer = 0
        for a, b in zip(nums1, nums2):
            current = defaultdict(int)
            current[a] += 1
            current[-b] += 1
            for difference, count in previous.items():
                current[difference + a] = (current[difference + a] + count) % mod
                current[difference - b] = (current[difference - b] + count) % mod
            answer = (answer + current[0]) % mod
            previous = current
        return answer
