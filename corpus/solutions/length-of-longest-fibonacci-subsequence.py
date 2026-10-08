class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        positions = {value: i for i, value in enumerate(arr)}
        dp: Dict[Tuple[int, int], int] = {}
        answer = 0
        for right, value in enumerate(arr):
            for middle in range(right):
                first = value - arr[middle]
                left = positions.get(first, right)
                if left < middle:
                    length = dp.get((left, middle), 2) + 1
                    dp[(middle, right)] = length
                    answer = max(answer, length)
        return answer
