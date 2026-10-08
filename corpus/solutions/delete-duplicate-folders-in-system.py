from collections import Counter


class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        children: list[dict[str, int]] = [{}]
        for path in paths:
            node = 0
            for name in path:
                if name not in children[node]:
                    children[node][name] = len(children)
                    children.append({})
                node = children[node][name]
        signatures = [0] * len(children)
        intern: dict[tuple[tuple[str, int], ...], int] = {}
        frequency: Counter[int] = Counter()
        # Children are created after their parent, so reverse order is postorder.
        for node in range(len(children) - 1, 0, -1):
            if children[node]:
                key = tuple(
                    sorted(
                        (name, signatures[ch]) for name, ch in children[node].items()
                    )
                )
                if key not in intern:
                    intern[key] = len(intern) + 1
                signatures[node] = intern[key]
                frequency[signatures[node]] += 1
        result = []
        stack = [(0, [])]
        while stack:
            node, path = stack.pop()
            for name, ch in children[node].items():
                if signatures[ch] and frequency[signatures[ch]] > 1:
                    continue
                current = path + [name]
                result.append(current)
                stack.append((ch, current))
        return sorted(result)
