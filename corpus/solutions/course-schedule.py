class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        outgoing: list[list[int]] = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, prerequisite in prerequisites:
            outgoing[prerequisite].append(course)
            indegree[course] += 1
        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1
            for dependent in outgoing[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        return completed == numCourses
