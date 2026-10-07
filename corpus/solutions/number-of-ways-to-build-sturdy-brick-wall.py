class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        mod = 10**9 + 7
        patterns: list[frozenset[int]] = []

        def build(position: int, joints: tuple[int, ...]) -> None:
            if position == width:
                patterns.append(frozenset(joints))
                return
            for brick in bricks:
                next_position = position + brick
                if next_position <= width:
                    next_joints = joints + (
                        (next_position,) if next_position < width else ()
                    )
                    build(next_position, next_joints)

        build(0, ())
        if not patterns:
            return 0
        compatible = [
            [i for i, other in enumerate(patterns) if not pattern & other]
            for pattern in patterns
        ]
        ways = [1] * len(patterns)
        for _ in range(1, height):
            next_ways = [
                sum(ways[j] for j in compatible[i]) % mod for i in range(len(patterns))
            ]
            ways = next_ways
        return sum(ways) % mod
