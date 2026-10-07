class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = set()
        next_suffix = {}
        answer = []
        for name in names:
            if name not in used:
                assigned = name
                next_suffix.setdefault(name, 1)
            else:
                suffix = next_suffix.get(name, 1)
                assigned = f"{name}({suffix})"
                while assigned in used:
                    suffix += 1
                    assigned = f"{name}({suffix})"
                next_suffix[name] = suffix + 1
                next_suffix.setdefault(assigned, 1)
            used.add(assigned)
            answer.append(assigned)
        return answer
