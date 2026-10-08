class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, list[str]] = defaultdict(list)
        for word in strs:
            groups["".join(sorted(word))].append(word)
        return sorted((sorted(group) for group in groups.values()))
