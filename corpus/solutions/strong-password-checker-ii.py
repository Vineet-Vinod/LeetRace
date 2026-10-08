class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        specials = "!@#$%^&*()-+"
        return (
            len(password) >= 8
            and any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in specials for c in password)
            and all(a != b for a, b in zip(password, password[1:]))
        )
