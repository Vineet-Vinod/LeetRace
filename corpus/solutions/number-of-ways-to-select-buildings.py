class Solution:
    def numberOfWays(self, s: str) -> int:
        total0 = s.count("0")
        total1 = len(s) - total0
        seen0 = seen1 = answer = 0
        for char in s:
            if char == "0":
                answer += seen1 * (total1 - seen1)
                seen0 += 1
            else:
                answer += seen0 * (total0 - seen0)
                seen1 += 1
        return answer
