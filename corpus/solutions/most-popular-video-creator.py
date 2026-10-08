class Solution:
    def mostPopularCreator(
        self, creators: List[str], ids: List[str], views: List[int]
    ) -> List[List[str]]:
        totals = {}
        best_video = {}
        for creator, video, view_count in zip(creators, ids, views):
            totals[creator] = totals.get(creator, 0) + view_count
            current = best_video.get(creator)
            if (
                current is None
                or view_count > current[0]
                or (view_count == current[0] and video < current[1])
            ):
                best_video[creator] = (view_count, video)
        maximum = max(totals.values())
        return [
            [creator, best_video[creator][1]]
            for creator in sorted(totals)
            if totals[creator] == maximum
        ]
