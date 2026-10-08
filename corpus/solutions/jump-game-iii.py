class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        seen = {start}
        stack = [start]
        while stack:
            index = stack.pop()
            if arr[index] == 0:
                return True
            for next_index in (index - arr[index], index + arr[index]):
                if 0 <= next_index < len(arr) and next_index not in seen:
                    seen.add(next_index)
                    stack.append(next_index)
        return False
