class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent: Dict[str, str] = {}
        owner: Dict[str, str] = {}

        def find(x: str) -> str:
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                owner[email] = name
                find(email)
            for email in emails[1:]:
                parent[find(email)] = find(emails[0])
        groups: Dict[str, List[str]] = {}
        for email in owner:
            groups.setdefault(find(email), []).append(email)
        result = [[owner[root], *sorted(emails)] for root, emails in groups.items()]
        return sorted(result)
