class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result: set[Tuple[int, ...]] = set()

        def search(index: int, path: List[int]) -> None:
            if len(path) >= 2:
                result.add(tuple(path))
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                if not path or nums[i] >= path[-1]:
                    search(i + 1, path + [nums[i]])

        search(0, [])
        return [list(sequence) for sequence in sorted(result)]
