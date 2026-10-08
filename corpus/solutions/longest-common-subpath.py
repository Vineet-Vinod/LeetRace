class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        base = min(paths, key=len)
        transitions = [{}]
        link = [-1]
        length = [0]
        last = 0
        for city in base:
            current = len(length)
            length.append(length[last] + 1)
            transitions.append({})
            link.append(0)
            p = last
            while p != -1 and city not in transitions[p]:
                transitions[p][city] = current
                p = link[p]
            if p != -1:
                q = transitions[p][city]
                if length[p] + 1 == length[q]:
                    link[current] = q
                else:
                    clone = len(length)
                    length.append(length[p] + 1)
                    transitions.append(transitions[q].copy())
                    link.append(link[q])
                    while p != -1 and transitions[p].get(city) == q:
                        transitions[p][city] = clone
                        p = link[p]
                    link[q] = link[current] = clone
            last = current
        common = length.copy()
        order = sorted(range(1, len(length)), key=lambda i: length[i], reverse=True)
        for path in paths:
            best = [0] * len(length)
            state = matched = 0
            for city in path:
                while state and city not in transitions[state]:
                    state = link[state]
                    matched = length[state]
                if city in transitions[state]:
                    state = transitions[state][city]
                    matched += 1
                else:
                    state = matched = 0
                best[state] = max(best[state], matched)
            for state in order:
                parent = link[state]
                best[parent] = max(best[parent], min(best[state], length[parent]))
            common = [min(a, b) for a, b in zip(common, best)]
        return max(common)
