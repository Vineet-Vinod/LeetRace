class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        for word in dict:
            for index in range(len(word)):
                signature = (index, word[:index], word[index + 1 :])
                if signature in seen:
                    return True
                seen.add(signature)
        return False
