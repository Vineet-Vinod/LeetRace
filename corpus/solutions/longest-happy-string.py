class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = [a, b, c]
        heap = [(-count, char) for char, count in zip("abc", counts) if count]
        heapify(heap)
        result = []
        while heap:
            count, char = heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == char:
                if not heap:
                    break
                next_count, next_char = heappop(heap)
                result.append(next_char)
                next_count += 1
                if next_count < 0:
                    heappush(heap, (next_count, next_char))
                heappush(heap, (count, char))
            else:
                result.append(char)
                count += 1
                if count < 0:
                    heappush(heap, (count, char))
        return "".join(result)
