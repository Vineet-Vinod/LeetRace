class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target: list[int] = []
        for value, position in zip(nums, index):
            target.insert(position, value)
        return target
