class Solution:
    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        pairs = []
        for wi, (wx, wy) in enumerate(workers):
            for bi, (bx, by) in enumerate(bikes):
                pairs.append((abs(wx - bx) + abs(wy - by), wi, bi))
        answer = [-1] * len(workers)
        used_workers = set()
        used_bikes = set()
        for _, wi, bi in sorted(pairs):
            if wi not in used_workers and bi not in used_bikes:
                answer[wi] = bi
                used_workers.add(wi)
                used_bikes.add(bi)
                if len(used_workers) == len(workers):
                    break
        return answer
