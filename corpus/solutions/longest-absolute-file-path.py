class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lengths = {0: 0}
        longest = 0
        for entry in input.split("\n"):
            depth = entry.count("\t")
            name = entry[depth:]
            path_length = lengths[depth] + len(name)
            if "." in name:
                longest = max(longest, path_length)
            else:
                lengths[depth + 1] = path_length + 1
        return longest
