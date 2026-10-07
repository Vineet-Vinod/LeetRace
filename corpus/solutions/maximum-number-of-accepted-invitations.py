class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        girls = len(grid)
        boys = len(grid[0])
        assigned = [-1] * boys

        def augment(girl, visited):
            for boy in range(boys):
                if grid[girl][boy] and not visited[boy]:
                    visited[boy] = True
                    if assigned[boy] == -1 or augment(assigned[boy], visited):
                        assigned[boy] = girl
                        return True
            return False

        return sum(augment(girl, [False] * boys) for girl in range(girls))
