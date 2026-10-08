class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        products.sort()
        answer = []
        prefix = ""
        for char in searchWord:
            prefix += char
            start = bisect_left(products, prefix)
            matches = []
            for product in products[start : start + 3]:
                if product.startswith(prefix):
                    matches.append(product)
                else:
                    break
            answer.append(matches)
        return answer
