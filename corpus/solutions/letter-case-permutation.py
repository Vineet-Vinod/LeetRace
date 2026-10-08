class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        results = [""]
        for char in s:
            if char.isalpha():
                results = [
                    prefix + option
                    for prefix in results
                    for option in (char.lower(), char.upper())
                ]
            else:
                results = [prefix + char for prefix in results]
        return sorted(results)
