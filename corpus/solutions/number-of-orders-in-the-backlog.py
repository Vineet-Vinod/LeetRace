class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buys: list[tuple[int, int]] = []
        sells: list[tuple[int, int]] = []
        for price, amount, order_type in orders:
            if order_type == 0:
                while amount and sells and sells[0][0] <= price:
                    sell_price, sell_amount = heappop(sells)
                    traded = min(amount, sell_amount)
                    amount -= traded
                    sell_amount -= traded
                    if sell_amount:
                        heappush(sells, (sell_price, sell_amount))
                if amount:
                    heappush(buys, (-price, amount))
            else:
                while amount and buys and -buys[0][0] >= price:
                    buy_price, buy_amount = heappop(buys)
                    traded = min(amount, buy_amount)
                    amount -= traded
                    buy_amount -= traded
                    if buy_amount:
                        heappush(buys, (buy_price, buy_amount))
                if amount:
                    heappush(sells, (price, amount))
        return sum(amount for _, amount in buys + sells) % (10**9 + 7)
