class Solution:
    def betterCompression(self, compressed: str) -> str:
        totals = [0] * 26
        index = 0
        while index < len(compressed):
            letter = compressed[index]
            index += 1
            start = index
            while index < len(compressed) and compressed[index].isdigit():
                index += 1
            totals[ord(letter) - ord("a")] += int(compressed[start:index])
        return "".join(
            chr(ord("a") + i) + str(count) for i, count in enumerate(totals) if count
        )
