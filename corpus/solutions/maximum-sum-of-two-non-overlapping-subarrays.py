class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def ordered(left_len: int, right_len: int) -> int:
            prefix = [0]
            for value in nums:
                prefix.append(prefix[-1] + value)
            best_left = 0
            answer = 0
            for right_start in range(left_len, len(nums) - right_len + 1):
                left_sum = prefix[right_start] - prefix[right_start - left_len]
                best_left = max(best_left, left_sum)
                right_sum = prefix[right_start + right_len] - prefix[right_start]
                answer = max(answer, best_left + right_sum)
            return answer

        return max(ordered(firstLen, secondLen), ordered(secondLen, firstLen))
