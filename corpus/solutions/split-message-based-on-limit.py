from typing import List


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        digits_sum = 0
        for parts in range(1, len(message) + 1):
            digits_sum += len(str(parts))
            suffix_length = 3 + 2 * len(str(parts))
            if suffix_length >= limit:
                break
            capacity = parts * (limit - 3 - len(str(parts))) - digits_sum
            if capacity < len(message):
                continue
            answer = []
            position = 0
            for i in range(1, parts + 1):
                suffix = f"<{i}/{parts}>"
                size = limit - len(suffix)
                answer.append(message[position : position + size] + suffix)
                position += size
            return answer
        return []
