class Solution:
    def watchedVideosByFriends(
        self,
        watchedVideos: List[List[str]],
        friends: List[List[int]],
        id: int,
        level: int,
    ) -> List[str]:
        visited = {id}
        frontier = [id]
        for _ in range(level):
            next_frontier: list[int] = []
            for person in frontier:
                for friend in friends[person]:
                    if friend not in visited:
                        visited.add(friend)
                        next_frontier.append(friend)
            frontier = next_frontier
        counts = Counter(
            video for person in frontier for video in watchedVideos[person]
        )
        return sorted(counts, key=lambda video: (counts[video], video))
