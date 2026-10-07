class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for index in range(len(arr) - 1, -1, -1):
            value = arr[index]
            arr[index] = greatest
            greatest = max(greatest, value)
        return arr
