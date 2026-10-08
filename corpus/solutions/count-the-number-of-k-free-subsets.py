class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        groups: dict[int, list[int]] = defaultdict(list)
        for value in nums:
            groups[value % k].append(value)
        total = 1
        for values in groups.values():
            values.sort()
            ways = 1
            start = 0
            while start < len(values):
                end = start + 1
                while end < len(values) and values[end] - values[end - 1] == k:
                    end += 1
                take, skip = 0, 1
                for _ in values[start:end]:
                    take, skip = skip, take + skip
                ways *= take + skip
                start = end
            total *= ways
        return total
