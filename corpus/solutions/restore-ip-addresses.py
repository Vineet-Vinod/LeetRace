class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def search(index: int, parts: List[str]) -> None:
            remaining = len(s) - index
            slots = 4 - len(parts)
            if remaining < slots or remaining > 3 * slots:
                return
            if slots == 0:
                if index == len(s):
                    result.append(".".join(parts))
                return
            for size in range(1, 4):
                piece = s[index : index + size]
                if (
                    len(piece) != size
                    or (size > 1 and piece[0] == "0")
                    or int(piece) > 255
                ):
                    continue
                search(index + size, parts + [piece])

        search(0, [])
        return sorted(result)
