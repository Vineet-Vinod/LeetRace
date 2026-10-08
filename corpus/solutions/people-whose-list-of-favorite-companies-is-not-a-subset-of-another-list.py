class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(companies) for companies in favoriteCompanies]
        answer = []
        for i, current in enumerate(sets):
            if not any(current < other for j, other in enumerate(sets) if i != j):
                answer.append(i)
        return answer
