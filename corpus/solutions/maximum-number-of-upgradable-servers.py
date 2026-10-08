class Solution:
    def maxUpgrades(
        self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]
    ) -> List[int]:
        answer = []
        for servers, cost, sale, budget in zip(count, upgrade, sell, money):
            answer.append(min(servers, (budget + servers * sale) // (cost + sale)))
        return answer
