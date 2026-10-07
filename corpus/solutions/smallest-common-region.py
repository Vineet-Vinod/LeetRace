class Solution:
    def findSmallestRegion(
        self, regions: List[List[str]], region1: str, region2: str
    ) -> str:
        parent: dict[str, str] = {}
        for group in regions:
            for child in group[1:]:
                parent[child] = group[0]
        ancestors = set()
        current = region1
        while current in parent:
            ancestors.add(current)
            current = parent[current]
        ancestors.add(current)
        current = region2
        while current not in ancestors:
            current = parent[current]
        return current
