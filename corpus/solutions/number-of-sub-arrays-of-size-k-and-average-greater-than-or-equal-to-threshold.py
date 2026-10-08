class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        window = sum(arr[:k])
        answer = int(window >= target)
        for right in range(k, len(arr)):
            window += arr[right] - arr[right - k]
            answer += window >= target
        return answer
