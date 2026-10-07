class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        normalized = set()
        for email in emails:
            local, domain = email.split("@")
            normalized.add(local.split("+")[0].replace(".", "") + "@" + domain)
        return len(normalized)
