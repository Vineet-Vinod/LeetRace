class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        differences = [i for i, (a, b) in enumerate(zip(s, goal)) if a != b]
        if not differences:
            return len(set(s)) < len(s)
        if len(differences) != 2:
            return False
        i, j = differences
        return s[i] == goal[j] and s[j] == goal[i]
