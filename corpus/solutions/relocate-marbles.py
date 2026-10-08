class Solution:
    def relocateMarbles(
        self, nums: List[int], moveFrom: List[int], moveTo: List[int]
    ) -> List[int]:
        occupied = set(nums)
        for source, target in zip(moveFrom, moveTo):
            occupied.remove(source)
            occupied.add(target)
        return sorted(occupied)
