from array import array


class Solution:
    def canMakePalindromeQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s) // 2
        left, right = s[:n], s[n:][::-1]
        alphabet = sorted(set(s))

        def prefixes(text):
            result = []
            for c in alphabet:
                row = array("i", [0])
                total = 0
                for v in text:
                    total += v == c
                    row.append(total)
                result.append(row)
            return result

        p, q = prefixes(left), prefixes(right)
        mismatches = [0]
        for a, b in zip(left, right):
            mismatches.append(mismatches[-1] + (a != b))

        def counts(prefix, lo, hi):
            return (
                [row[hi + 1] - row[lo] for row in prefix]
                if lo <= hi
                else [0] * len(alphabet)
            )

        answer = []
        for a, b, c, d in queries:
            c, d = 2 * n - 1 - d, 2 * n - 1 - c
            lo, hi = max(a, c), min(b, d)
            covered = (
                mismatches[b + 1] - mismatches[a] + mismatches[d + 1] - mismatches[c]
            )
            if lo <= hi:
                covered -= mismatches[hi + 1] - mismatches[lo]
            if covered != mismatches[-1]:
                answer.append(False)
                continue
            available_left = counts(p, a, b)
            available_right = counts(q, c, d)
            required_left = counts(q, a, b)
            required_right = counts(p, c, d)
            shared_left = counts(p, lo, hi)
            shared_right = counts(q, lo, hi)
            valid = True
            for j in range(len(alphabet)):
                x = available_left[j] - required_left[j] + shared_right[j]
                y = available_right[j] - required_right[j] + shared_left[j]
                if x < 0 or y < 0 or x != y:
                    valid = False
                    break
            answer.append(valid)
        return answer
