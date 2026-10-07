class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half_length = (intLength + 1) // 2
        first_prefix = 10 ** (half_length - 1)
        limit = 10**half_length
        answers = []
        for query in queries:
            prefix = first_prefix + query - 1
            if prefix >= limit:
                answers.append(-1)
                continue
            left = str(prefix)
            right = left[:-1] if intLength % 2 else left
            answers.append(int(left + right[::-1]))
        return answers
