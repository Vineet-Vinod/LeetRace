class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        answer = 0

        def search(index: int, chosen: List[int]) -> None:
            nonlocal answer
            if index == len(nums):
                if chosen:
                    answer += 1
                return
            search(index + 1, chosen)
            value = nums[index]
            if all(abs(value - other) != k for other in chosen):
                chosen.append(value)
                search(index + 1, chosen)
                chosen.pop()

        search(0, [])
        return answer
