from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def palindrome_edges(word):
            n = len(word)
            odd = [0] * n
            even = [0] * n
            for radii, offset in ((odd, 1), (even, 0)):
                left, right = 0, -1
                for center in range(n):
                    radius = (
                        offset
                        if center > right
                        else min(
                            radii[left + right - center + 1 - offset],
                            right - center + 1,
                        )
                    )
                    while (
                        center - radius - 1 + offset >= 0
                        and center + radius < n
                        and word[center - radius - 1 + offset] == word[center + radius]
                    ):
                        radius += 1
                    radii[center] = radius
                    if center + radius - 1 > right:
                        left, right = center - radius + offset, center + radius - 1
            prefix = [False] * n
            suffix = [False] * (n + 1)
            suffix[n] = True
            for center in range(n):
                for radius, offset in ((odd[center], 1), (even[center], 0)):
                    start, end = center - radius + offset, center + radius - 1
                    if start == 0 and end >= 0:
                        prefix[end] = True
                    if end == n - 1:
                        suffix[start] = True
            return prefix, suffix

        children = [{}]
        terminal = [-1]
        palindromes = [[]]
        suffixes = []
        for index, word in enumerate(words):
            prefix, suffix = palindrome_edges(word)
            suffixes.append(suffix)
            node = 0
            for position in range(len(word) - 1, -1, -1):
                if prefix[position]:
                    palindromes[node].append(index)
                ch = word[position]
                if ch not in children[node]:
                    children[node][ch] = len(children)
                    children.append({})
                    terminal.append(-1)
                    palindromes.append([])
                node = children[node][ch]
            terminal[node] = index
            palindromes[node].append(index)
        result = []
        for index, word in enumerate(words):
            node = 0
            for position, ch in enumerate(word):
                other = terminal[node]
                if other != -1 and other != index and suffixes[index][position]:
                    result.append([index, other])
                if ch not in children[node]:
                    break
                node = children[node][ch]
            else:
                result.extend(
                    [index, other] for other in palindromes[node] if other != index
                )
        return sorted(result)
