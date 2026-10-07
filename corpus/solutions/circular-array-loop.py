class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for start in range(n):
            direction = nums[start] > 0
            seen: set[int] = set()
            current = start
            while current not in seen and (nums[current] > 0) == direction:
                seen.add(current)
                nxt = (current + nums[current]) % n
                if nxt == current:
                    break
                current = nxt
            else:
                if current in seen:
                    return True
        return False
