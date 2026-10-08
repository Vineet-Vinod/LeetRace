class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_index = abbreviation_index = 0
        while abbreviation_index < len(abbr):
            if abbr[abbreviation_index].isdigit():
                if abbr[abbreviation_index] == "0":
                    return False
                skipped = 0
                while (
                    abbreviation_index < len(abbr)
                    and abbr[abbreviation_index].isdigit()
                ):
                    skipped = skipped * 10 + int(abbr[abbreviation_index])
                    abbreviation_index += 1
                word_index += skipped
            else:
                if (
                    word_index >= len(word)
                    or word[word_index] != abbr[abbreviation_index]
                ):
                    return False
                word_index += 1
                abbreviation_index += 1
        return word_index == len(word)
