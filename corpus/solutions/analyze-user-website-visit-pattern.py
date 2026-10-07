class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        visits = {}
        for user, time, site in zip(username, timestamp, website):
            visits.setdefault(user, []).append((time, site))
        counts = {}
        for records in visits.values():
            sites = [site for _, site in sorted(records)]
            patterns = set()
            for i in range(len(sites)):
                for j in range(i + 1, len(sites)):
                    for k in range(j + 1, len(sites)):
                        patterns.add((sites[i], sites[j], sites[k]))
            for pattern in patterns:
                counts[pattern] = counts.get(pattern, 0) + 1
        best_count = max(counts.values())
        return list(
            min(pattern for pattern, count in counts.items() if count == best_count)
        )
