class Solution:
    def maxNumberOfAlloys(
        self,
        n: int,
        k: int,
        budget: int,
        composition: List[List[int]],
        stock: List[int],
        cost: List[int],
    ) -> int:
        answer = 0
        for machine in composition:
            low, high = 0, min((stock[i] + budget) // machine[i] for i in range(n)) + 1
            while low + 1 < high:
                amount = (low + high) // 2
                required = sum(
                    max(0, amount * machine[i] - stock[i]) * cost[i] for i in range(n)
                )
                if required <= budget:
                    low = amount
                else:
                    high = amount
            answer = max(answer, low)
        return answer
