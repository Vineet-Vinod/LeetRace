class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        rotate = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        def count(bound: int) -> int:
            if bound < 0:
                return 0
            text = str(bound)
            answer = 0
            for length in range(1, len(text) + 1):
                choices = []
                for i in range((length + 1) // 2):
                    if i == length - 1 - i:
                        choices.append("018")
                    elif i == 0:
                        choices.append("1689")
                    else:
                        choices.append("01689")
                if length < len(text):
                    product = 1
                    for digits in choices:
                        product *= len(digits)
                    answer += product
                    continue
                prefix = ""
                for i, digits in enumerate(choices):
                    product = 1
                    for remaining in choices[i + 1 :]:
                        product *= len(remaining)
                    answer += sum(d < text[i] for d in digits) * product
                    if text[i] not in digits:
                        break
                    prefix += text[i]
                else:
                    tail = prefix[:-1] if length % 2 else prefix
                    formed = prefix + "".join(rotate[d] for d in reversed(tail))
                    answer += formed <= text
            return answer

        return count(int(high)) - count(int(low) - 1)
