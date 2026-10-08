class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        times: Dict[str, List[int]] = defaultdict(list)
        for name, stamp in zip(keyName, keyTime):
            h, m = map(int, stamp.split(":"))
            times[name].append(60 * h + m)
        result = []
        for name, vals in times.items():
            vals.sort()
            if any(vals[i + 2] - vals[i] <= 60 for i in range(len(vals) - 2)):
                result.append(name)
        return sorted(result)
