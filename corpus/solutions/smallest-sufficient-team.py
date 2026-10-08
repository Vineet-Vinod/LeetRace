class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        bits = {skill: 1 << i for i, skill in enumerate(req_skills)}
        dp = {0: ()}
        for i, skills in enumerate(people):
            mask = sum(bits[skill] for skill in skills)
            for previous, team in list(dp.items()):
                combined = previous | mask
                candidate = team + (i,)
                if combined not in dp or (len(candidate), candidate) < (
                    len(dp[combined]),
                    dp[combined],
                ):
                    dp[combined] = candidate
        return list(dp[(1 << len(req_skills)) - 1])
