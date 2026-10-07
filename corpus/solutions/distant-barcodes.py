class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counts = Counter(barcodes)
        ordered = sorted(counts, key=lambda value: (-counts[value], value))
        result = [0] * len(barcodes)
        index = 0
        for value in ordered:
            for _ in range(counts[value]):
                if index >= len(result):
                    index = 1
                result[index] = value
                index += 2
        return result
