class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split(" ")
        converted = []
        for index, word in enumerate(words, 1):
            if word[0] not in vowels:
                word = word[1:] + word[0]
            converted.append(word + "ma" + "a" * index)
        return " ".join(converted)
