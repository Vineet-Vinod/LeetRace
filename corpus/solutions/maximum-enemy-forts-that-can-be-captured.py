class Solution:
    def captureForts(self, forts: List[int]) -> int:
        best = 0
        last_fort = None
        for index, fort in enumerate(forts):
            if fort:
                if last_fort is not None and fort != forts[last_fort]:
                    best = max(best, index - last_fort - 1)
                last_fort = index
        return best
