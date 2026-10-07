class Solution:
    def expand(self, s: str) -> List[str]:
        options: List[List[str]] = []
        i = 0
        while i < len(s):
            if s[i] == "{":
                end = s.index("}", i)
                options.append(s[i + 1 : end].split(","))
                i = end + 1
            else:
                options.append([s[i]])
                i += 1
        return sorted({"".join(parts) for parts in product(*options)})
