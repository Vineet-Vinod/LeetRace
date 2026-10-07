class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        sequence = [0] * (2 * n - 1)
        used = [False] * (n + 1)

        def search(index):
            while index < len(sequence) and sequence[index] != 0:
                index += 1
            if index == len(sequence):
                return True
            for value in range(n, 0, -1):
                if used[value]:
                    continue
                other = index if value == 1 else index + value
                if other >= len(sequence) or sequence[other] != 0:
                    continue
                sequence[index] = value
                sequence[other] = value
                used[value] = True
                if search(index + 1):
                    return True
                sequence[index] = sequence[other] = 0
                used[value] = False
            return False

        search(0)
        return sequence
