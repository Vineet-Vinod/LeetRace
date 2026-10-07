class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        offers = []
        for offer in special:
            quantities = offer[:-1]
            if any(quantities) and offer[-1] < sum(
                q * p for q, p in zip(quantities, price)
            ):
                offers.append((quantities, offer[-1]))

        @lru_cache(None)
        def solve(remaining):
            best = sum(q * p for q, p in zip(remaining, price))
            for quantities, cost in offers:
                next_needs = tuple(
                    need - quantity for need, quantity in zip(remaining, quantities)
                )
                if min(next_needs, default=0) >= 0:
                    best = min(best, cost + solve(next_needs))
            return best

        return solve(tuple(needs))
