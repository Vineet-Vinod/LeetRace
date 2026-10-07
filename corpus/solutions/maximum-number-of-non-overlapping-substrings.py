class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        first = {}
        last = {}
        for i, c in enumerate(s):
            first.setdefault(c, i)
            last[c] = i
        intervals = []
        for c, left in first.items():
            right = last[c]
            i = left
            valid = True
            while i <= right:
                if first[s[i]] < left:
                    valid = False
                    break
                right = max(right, last[s[i]])
                i += 1
            if valid:
                intervals.append((right, left))
        chosen = []
        end = -1
        for right, left in sorted(intervals):
            if left > end:
                chosen.append(s[left : right + 1])
                end = right
        return chosen
