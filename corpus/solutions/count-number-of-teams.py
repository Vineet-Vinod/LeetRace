class Solution:
    def numTeams(self, rating: List[int]) -> int:
        total = 0
        for middle in range(len(rating)):
            left_less = sum(value < rating[middle] for value in rating[:middle])
            left_greater = middle - left_less
            right_less = sum(value < rating[middle] for value in rating[middle + 1 :])
            right_greater = len(rating) - middle - 1 - right_less
            total += left_less * right_greater + left_greater * right_less
        return total
