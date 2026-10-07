class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        pair_counts: Dict[int, int] = {}
        answer = 0
        for last in range(2, len(nums)):
            middle = last - 1
            for first in range(middle):
                residue = (nums[first] + nums[middle]) % d
                pair_counts[residue] = pair_counts.get(residue, 0) + 1
            answer += pair_counts.get((-nums[last]) % d, 0)
        return answer
