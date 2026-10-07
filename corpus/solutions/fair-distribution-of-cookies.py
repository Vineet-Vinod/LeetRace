class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bags = sorted(cookies, reverse=True)
        loads = [0] * k
        best = sum(bags)

        def search(index):
            nonlocal best
            if index == len(bags):
                best = min(best, max(loads))
                return
            if max(loads) >= best:
                return
            amount = bags[index]
            tried = set()
            for child in range(k):
                if loads[child] in tried:
                    continue
                tried.add(loads[child])
                loads[child] += amount
                search(index + 1)
                loads[child] -= amount
                if loads[child] == 0:
                    break

        search(0)
        return best
