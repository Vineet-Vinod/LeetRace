class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        parent = list(range(n))
        size = [1] * n
        components = n

        def find(person: int) -> int:
            while parent[person] != person:
                parent[person] = parent[parent[person]]
                person = parent[person]
            return person

        for timestamp, first, second in sorted(logs):
            root_first, root_second = find(first), find(second)
            if root_first != root_second:
                if size[root_first] < size[root_second]:
                    root_first, root_second = root_second, root_first
                parent[root_second] = root_first
                size[root_first] += size[root_second]
                components -= 1
                if components == 1:
                    return timestamp
        return -1
