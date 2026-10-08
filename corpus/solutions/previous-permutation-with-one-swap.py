class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        result = arr[:]
        pivot = len(result) - 2
        while pivot >= 0 and result[pivot] <= result[pivot + 1]:
            pivot -= 1
        if pivot < 0:
            return result
        swap_index = len(result) - 1
        while result[swap_index] >= result[pivot]:
            swap_index -= 1
        while swap_index > pivot + 1 and result[swap_index] == result[swap_index - 1]:
            swap_index -= 1
        result[pivot], result[swap_index] = result[swap_index], result[pivot]
        return result
