class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ordered = sorted(nums)
        paths: list[tuple[int, ...]] = []
        for index, value in enumerate(ordered):
            best_path = (value,)
            for previous in range(index):
                if value % ordered[previous] != 0:
                    continue
                candidate = paths[previous] + (value,)
                if len(candidate) > len(best_path) or (
                    len(candidate) == len(best_path) and candidate < best_path
                ):
                    best_path = candidate
            paths.append(best_path)
        longest = max(paths, key=len)
        return list(min(path for path in paths if len(path) == len(longest)))
