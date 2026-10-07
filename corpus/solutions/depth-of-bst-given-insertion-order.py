class Solution:
    def maxDepthBST(self, order: list[int]) -> int:
        size = len(order)
        insertion_time = [0] * (size + 1)
        for time, value in enumerate(order, 1):
            insertion_time[value] = time
        left_child = [-1] * (size + 1)
        right_child = [-1] * (size + 1)
        stack: list[int] = []
        for value in range(1, size + 1):
            last = -1
            while stack and insertion_time[stack[-1]] > insertion_time[value]:
                last = stack.pop()
            if stack:
                right_child[stack[-1]] = value
            if last != -1:
                left_child[value] = last
            stack.append(value)
        root = stack[0]
        maximum = 0
        pending = [(root, 1)]
        while pending:
            value, depth = pending.pop()
            maximum = max(maximum, depth)
            if left_child[value] != -1:
                pending.append((left_child[value], depth + 1))
            if right_child[value] != -1:
                pending.append((right_child[value], depth + 1))
        return maximum
