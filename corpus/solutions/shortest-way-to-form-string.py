class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_letters = set(source)
        if any(char not in source_letters for char in target):
            return -1
        scans = 0
        position = 0
        while position < len(target):
            scans += 1
            source_index = 0
            while source_index < len(source) and position < len(target):
                if source[source_index] == target[position]:
                    position += 1
                source_index += 1
        return scans
