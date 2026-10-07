class Solution:
    def minAbbreviation(self, target: str, dictionary: list[str]) -> str:
        m = len(target)
        full = (1 << m) - 1
        differences = []
        for word in dictionary:
            if len(word) == m:
                differences.append(
                    sum(1 << i for i in range(m) if target[i] != word[i])
                )
        if not differences:
            return str(m)
        best = target
        cost = m
        for mask in range(1 << m):
            omitted = full ^ mask
            length = mask.bit_count() + (omitted & ~(omitted << 1)).bit_count()
            if length > cost or any(mask & d == 0 for d in differences):
                continue
            parts = []
            run = 0
            for i, c in enumerate(target):
                if mask >> i & 1:
                    if run:
                        parts.append(str(run))
                        run = 0
                    parts.append(c)
                else:
                    run += 1
            if run:
                parts.append(str(run))
            abbreviation = "".join(parts)
            if length < cost or abbreviation < best:
                cost = length
                best = abbreviation
        return best
