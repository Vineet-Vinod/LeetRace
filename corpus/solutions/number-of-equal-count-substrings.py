class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        answer = 0
        for distinct in range(1, 27):
            width = distinct * count
            if width > len(s):
                break
            freq = [0] * 26
            good = 0
            for i, ch in enumerate(s):
                x = ord(ch) - 97
                freq[x] += 1
                if freq[x] == count:
                    good += 1
                elif freq[x] == count + 1:
                    good -= 1
                if i >= width:
                    y = ord(s[i - width]) - 97
                    if freq[y] == count:
                        good -= 1
                    elif freq[y] == count + 1:
                        good += 1
                    freq[y] -= 1
                if i + 1 >= width and good == distinct:
                    answer += 1
        return answer
