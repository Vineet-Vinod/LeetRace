class Solution:
    def minSwaps(self, s: str) -> int:
        zeros = s.count("0")
        ones = len(s) - zeros
        if abs(zeros - ones) > 1:
            return -1

        def mismatches(first):
            return sum(
                char != ("0" if i % 2 == 0 else "1")
                if first == "0"
                else char != ("1" if i % 2 == 0 else "0")
                for i, char in enumerate(s)
            )

        choices = []
        if zeros >= ones:
            choices.append(mismatches("0") // 2)
        if ones >= zeros:
            choices.append(mismatches("1") // 2)
        return min(choices)
