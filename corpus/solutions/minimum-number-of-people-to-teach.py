class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        known = [set(values) for values in languages]
        users = set()
        for first, second in friendships:
            if known[first - 1].isdisjoint(known[second - 1]):
                users.add(first - 1)
                users.add(second - 1)
        if not users:
            return 0
        return min(
            sum(language not in known[user] for user in users)
            for language in range(1, n + 1)
        )
