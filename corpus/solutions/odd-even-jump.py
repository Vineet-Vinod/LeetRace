from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        def successors(order):
            result = [-1] * n
            stack = []
            for i in order:
                while stack and stack[-1] < i:
                    result[stack.pop()] = i
                stack.append(i)
            return result

        odd_next = successors(sorted(range(n), key=lambda i: (arr[i], i)))
        even_next = successors(sorted(range(n), key=lambda i: (-arr[i], i)))
        odd, even = [False] * n, [False] * n
        odd[-1] = even[-1] = True
        for i in range(n - 2, -1, -1):
            if odd_next[i] != -1:
                odd[i] = even[odd_next[i]]
            if even_next[i] != -1:
                even[i] = odd[even_next[i]]
        return sum(odd)
