class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        answer = 0
        for value in nums:
            divisor_sum = 1 + value
            divisor_count = 2
            divisor = 2
            while divisor * divisor <= value and divisor_count <= 4:
                if value % divisor == 0:
                    other = value // divisor
                    divisor_count += 1 if divisor == other else 2
                    divisor_sum += divisor + (other if other != divisor else 0)
                divisor += 1
            if divisor_count == 4:
                answer += divisor_sum
        return answer
