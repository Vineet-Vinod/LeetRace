from typing import List


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        trie = [[-1, -1, 0]]

        def less(x, bound):
            node, total = 0, 0
            for bit in range(15, -1, -1):
                if node < 0:
                    break
                b = (x >> bit) & 1
                if (bound >> bit) & 1:
                    same = trie[node][b]
                    if same >= 0:
                        total += trie[same][2]
                    node = trie[node][1 - b]
                else:
                    node = trie[node][b]
            return total

        answer = 0
        for x in nums:
            answer += less(x, high + 1) - less(x, low)
            node = 0
            for bit in range(15, -1, -1):
                b = (x >> bit) & 1
                if trie[node][b] < 0:
                    trie[node][b] = len(trie)
                    trie.append([-1, -1, 0])
                node = trie[node][b]
                trie[node][2] += 1
        return answer
