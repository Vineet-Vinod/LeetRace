from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["$"] = word
        grid = [row[:] for row in board]
        m, n = len(grid), len(grid[0])
        found = set()

        def search(r, c, parent):
            ch = grid[r][c]
            if ch not in parent:
                return
            node = parent[ch]
            if "$" in node:
                found.add(node.pop("$"))
            grid[r][c] = "#"
            for a, b in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= a < m and 0 <= b < n and grid[a][b] in node:
                    search(a, b, node)
            grid[r][c] = ch
            if not node:
                del parent[ch]

        for r in range(m):
            for c in range(n):
                search(r, c, trie)
        return sorted(found)
