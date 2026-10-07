class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        reachable = [[False] * numCourses for _ in range(numCourses)]
        for before, after in prerequisites:
            reachable[before][after] = True
        for middle in range(numCourses):
            for start in range(numCourses):
                if reachable[start][middle]:
                    for end in range(numCourses):
                        reachable[start][end] = (
                            reachable[start][end] or reachable[middle][end]
                        )
        return [reachable[start][end] for start, end in queries]
