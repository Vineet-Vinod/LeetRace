class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        forbidden = {front for front, back in zip(fronts, backs) if front == back}
        candidates = [
            value
            for pair in zip(fronts, backs)
            for value in pair
            if value not in forbidden
        ]
        return min(candidates, default=0)
