class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing = (
            int(not any(c.islower() for c in password))
            + int(not any(c.isupper() for c in password))
            + int(not any(c.isdigit() for c in password))
        )
        runs = []
        i = 0
        while i < n:
            j = i + 1
            while j < n and password[j] == password[i]:
                j += 1
            if j - i >= 3:
                runs.append(j - i)
            i = j
        replacements = sum(x // 3 for x in runs)
        if n < 6:
            return max(6 - n, missing)
        if n <= 20:
            return max(missing, replacements)
        deletions = n - 20
        remaining = deletions
        for residue, required in ((0, 1), (1, 2)):
            for length in runs:
                if length % 3 == residue and remaining >= required:
                    replacements -= 1
                    remaining -= required
        replacements -= min(replacements, remaining // 3)
        return deletions + max(missing, replacements)
