class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        if any(len(word) > cols for word in sentence):
            return 0
        cycle = " ".join(sentence) + " "
        offset = 0
        for _ in range(rows):
            offset += cols
            if cycle[offset % len(cycle)] == " ":
                offset += 1
            else:
                while offset > 0 and cycle[(offset - 1) % len(cycle)] != " ":
                    offset -= 1
        return offset // len(cycle)
