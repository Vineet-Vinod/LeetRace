class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.split("@")
            return name[0].lower() + "*****" + name[-1].lower() + "@" + domain.lower()
        digits = "".join(char for char in s if char.isdigit())
        country = len(digits) - 10
        prefix = "+" + "*" * country + "-" if country else ""
        return prefix + "***-***-" + digits[-4:]
