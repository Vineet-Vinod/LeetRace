class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counts = Counter(s)
        maximum = max(counts.values())
        final_occurrences = {
            character: s.rfind(character)
            for character, count in counts.items()
            if count == maximum
        }
        final_position = max(final_occurrences.values())
        return "".join(
            character
            for index, character in enumerate(s)
            if final_occurrences.get(character) == index and index <= final_position
        )
