class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        size = len(code)
        if k == 0:
            return [0] * size
        doubled = code * 3
        prefix = [0]
        for value in doubled:
            prefix.append(prefix[-1] + value)
        result = []
        for i in range(size):
            if k > 0:
                left, right = size + i + 1, size + i + k + 1
            else:
                left, right = size + i + k, size + i
            result.append(prefix[right] - prefix[left])
        return result
