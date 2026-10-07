from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        allowed = set(bank)
        if endGene not in allowed:
            return -1
        queue = deque([(startGene, 0)])
        seen = {startGene}
        letters = "ACGT"
        while queue:
            gene, steps = queue.popleft()
            for index, current in enumerate(gene):
                for letter in letters:
                    if letter == current:
                        continue
                    neighbor = gene[:index] + letter + gene[index + 1 :]
                    if neighbor == endGene:
                        return steps + 1
                    if neighbor in allowed and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, steps + 1))
        return -1
