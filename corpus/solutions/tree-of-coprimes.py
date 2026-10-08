from math import gcd


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        adj = [[] for _ in nums]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        compatible = [[b for b in range(1, 51) if gcd(a, b) == 1] for a in range(51)]
        latest = [(-1, -1)] * 51
        answer = [-1] * n
        stack = [(0, -1, 0, False, (-1, -1))]
        while stack:
            u, parent, depth, exiting, old = stack.pop()
            value = nums[u]
            if exiting:
                latest[value] = old
                continue
            answer[u] = max((latest[b] for b in compatible[value]), default=(-1, -1))[1]
            stack.append((u, parent, depth, True, latest[value]))
            latest[value] = (depth, u)
            for v in adj[u]:
                if v != parent:
                    stack.append((v, u, depth + 1, False, (-1, -1)))
        return answer
