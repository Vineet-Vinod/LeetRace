class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        stack = []
        answer = 0
        for x in nums:
            while stack and stack[-1][0] < x:
                stack.pop()
            if stack and stack[-1][0] == x:
                value, count = stack.pop()
                stack.append((value, count + 1))
            else:
                stack.append((x, 1))
            answer += stack[-1][1]
        return answer
