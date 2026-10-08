from typing import List
from collections import deque


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        children = [{}]
        fail = [0]
        output = [-1]
        length = [0]
        price = [10**30]
        for word, cost in zip(words, costs):
            v = 0
            for ch in word:
                if ch not in children[v]:
                    children[v][ch] = len(children)
                    children.append({})
                    fail.append(0)
                    output.append(-1)
                    length.append(length[v] + 1)
                    price.append(10**30)
                v = children[v][ch]
            price[v] = min(price[v], cost)
        q = deque(children[0].values())
        while q:
            v = q.popleft()
            for ch, u in children[v].items():
                f = fail[v]
                while f and ch not in children[f]:
                    f = fail[f]
                fail[u] = children[f].get(ch, 0)
                z = fail[u]
                output[u] = z if price[z] < 10**30 else output[z]
                q.append(u)
        dp = [0] + [10**30] * len(target)
        v = 0
        for i, ch in enumerate(target, 1):
            while v and ch not in children[v]:
                v = fail[v]
            v = children[v].get(ch, 0)
            u = v
            while u != -1:
                if price[u] < 10**30:
                    dp[i] = min(dp[i], dp[i - length[u]] + price[u])
                u = output[u]
        return dp[-1] if dp[-1] < 10**30 else -1
