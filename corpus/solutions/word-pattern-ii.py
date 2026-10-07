class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        mapping: Dict[str, str] = {}
        used = set()

        def search(pattern_index: int, string_index: int) -> bool:
            if pattern_index == len(pattern):
                return string_index == len(s)
            char = pattern[pattern_index]
            if char in mapping:
                word = mapping[char]
                return s.startswith(word, string_index) and search(
                    pattern_index + 1, string_index + len(word)
                )
            remaining_chars = len(pattern) - pattern_index - 1
            for end in range(string_index + 1, len(s) - remaining_chars + 1):
                word = s[string_index:end]
                if word in used:
                    continue
                mapping[char] = word
                used.add(word)
                if search(pattern_index + 1, end):
                    return True
                del mapping[char]
                used.remove(word)
            return False

        return search(0, 0)
