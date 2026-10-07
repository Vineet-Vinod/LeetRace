from builtins import pow


class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        n = len(prevRoom)
        mod = 10**9 + 7
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[prevRoom[i]].append(i)
        order = [0]
        for u in order:
            order.extend(children[u])
        sizes = [1] * n
        for u in reversed(order[1:]):
            sizes[prevRoom[u]] += sizes[u]
        fact = 1
        denominator = 1
        for i in range(1, n):
            fact = fact * i % mod
        for size in sizes[1:]:
            denominator = denominator * size % mod
        return fact * pow(denominator, mod - 2, mod) % mod
