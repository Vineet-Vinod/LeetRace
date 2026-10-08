class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

        def build(length: int) -> List[str]:
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            result = []
            for middle in build(length - 2):
                for left, right in pairs:
                    if length == n and left == "0":
                        continue
                    result.append(left + middle + right)
            return result

        return sorted(build(n))
