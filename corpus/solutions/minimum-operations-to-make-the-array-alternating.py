class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def top_two(values: List[int]) -> list[tuple[int, int]]:
            counts = Counter(values)
            return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:2]

        even = top_two(nums[::2])
        odd = top_two(nums[1::2])
        even += [(None, 0)] * (2 - len(even))
        odd += [(None, 0)] * (2 - len(odd))
        best = 0
        for even_value, even_count in even:
            for odd_value, odd_count in odd:
                if even_value != odd_value:
                    best = max(best, even_count + odd_count)
        return len(nums) - best
