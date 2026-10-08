class Solution:
    def minimizeConcatenatedLength(self, words: list[str]) -> int:
        states = {(words[0][0], words[0][-1]): len(words[0])}
        for word in words[1:]:
            next_states: dict[tuple[str, str], int] = {}
            for (first, last), length in states.items():
                append = (first, word[-1])
                prepend = (word[0], last)
                append_length = length + len(word) - (last == word[0])
                prepend_length = length + len(word) - (word[-1] == first)
                next_states[append] = min(next_states.get(append, 10**9), append_length)
                next_states[prepend] = min(
                    next_states.get(prepend, 10**9), prepend_length
                )
            states = next_states
        return min(states.values())
