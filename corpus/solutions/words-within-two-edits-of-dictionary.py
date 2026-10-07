class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        answer: list[str] = []
        for query in queries:
            if any(
                sum(a != b for a, b in zip(query, word)) <= 2 for word in dictionary
            ):
                answer.append(query)
        return answer
