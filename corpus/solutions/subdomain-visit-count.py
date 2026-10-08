class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts: dict[str, int] = {}
        for entry in cpdomains:
            count_text, domain = entry.split()
            count = int(count_text)
            labels = domain.split(".")
            for i in range(len(labels)):
                suffix = ".".join(labels[i:])
                counts[suffix] = counts.get(suffix, 0) + count
        return [f"{count} {domain}" for domain, count in sorted(counts.items())]
