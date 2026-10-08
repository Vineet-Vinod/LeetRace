class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        owners: dict[str, set[int]] = defaultdict(set)
        substrings: list[set[str]] = []
        for index, word in enumerate(arr):
            current: set[str] = set()
            for start in range(len(word)):
                for end in range(start + 1, len(word) + 1):
                    current.add(word[start:end])
            substrings.append(current)
            for substring in current:
                owners[substring].add(index)
        answer: list[str] = []
        for index, current in enumerate(substrings):
            candidates = [
                substring for substring in current if owners[substring] == {index}
            ]
            answer.append(
                min(candidates, key=lambda substring: (len(substring), substring))
                if candidates
                else ""
            )
        return answer
