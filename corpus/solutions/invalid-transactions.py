class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        invalid = [False] * len(transactions)
        for index, transaction in enumerate(transactions):
            name, time_text, amount_text, city = transaction.split(",")
            minute = int(time_text)
            amount = int(amount_text)
            parsed.append((name, minute, amount, city))
            if amount > 1000:
                invalid[index] = True
        for first in range(len(parsed)):
            name_a, time_a, _, city_a = parsed[first]
            for second in range(first + 1, len(parsed)):
                name_b, time_b, _, city_b = parsed[second]
                if name_a == name_b and city_a != city_b and abs(time_a - time_b) <= 60:
                    invalid[first] = True
                    invalid[second] = True
        return sorted(
            transaction
            for transaction, is_invalid in zip(transactions, invalid)
            if is_invalid
        )
