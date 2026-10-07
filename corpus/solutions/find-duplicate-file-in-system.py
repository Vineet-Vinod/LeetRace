class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        by_content = defaultdict(list)
        for entry in paths:
            parts = entry.split()
            directory = parts[0]
            for file in parts[1:]:
                name, content = file[:-1].split("(", 1)
                by_content[content].append(directory + "/" + name)
        groups = [sorted(files) for files in by_content.values() if len(files) > 1]
        return sorted(groups)
