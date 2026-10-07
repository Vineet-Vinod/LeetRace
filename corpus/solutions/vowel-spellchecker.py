class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        casefold: dict[str, str] = {}
        vowel: dict[str, str] = {}

        def key(word: str) -> str:
            return "".join("*" if char in "aeiou" else char for char in word.lower())

        for word in wordlist:
            casefold.setdefault(word.lower(), word)
            vowel.setdefault(key(word), word)
        result = []
        for query in queries:
            result.append(
                query
                if query in exact
                else casefold.get(query.lower(), vowel.get(key(query), ""))
            )
        return result
