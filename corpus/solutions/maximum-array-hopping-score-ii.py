class Solution:
    def maxScore(self, nums: List[int]) -> int:
        coordinates = sorted(set(nums[1:]))
        lines: List[Optional[Tuple[int, int]]] = [None] * (4 * len(coordinates))

        def evaluate(line: Tuple[int, int], x: int) -> int:
            return line[0] * x + line[1]

        def insert(new_line: Tuple[int, int], node: int, left: int, right: int) -> None:
            current = lines[node]
            if current is None:
                lines[node] = new_line
                return
            middle = (left + right) // 2
            if evaluate(new_line, coordinates[middle]) > evaluate(
                current, coordinates[middle]
            ):
                lines[node], new_line = new_line, current
                current = lines[node]
            if left == right:
                return
            if evaluate(new_line, coordinates[left]) > evaluate(
                current, coordinates[left]
            ):
                insert(new_line, node * 2, left, middle)
            elif evaluate(new_line, coordinates[right]) > evaluate(
                current, coordinates[right]
            ):
                insert(new_line, node * 2 + 1, middle + 1, right)

        def query(x: int, node: int, left: int, right: int) -> int:
            current = lines[node]
            best = evaluate(current, x) if current is not None else -(10**30)
            if left == right:
                return best
            middle = (left + right) // 2
            if x <= coordinates[middle]:
                return max(best, query(x, node * 2, left, middle))
            return max(best, query(x, node * 2 + 1, middle + 1, right))

        insert((0, 0), 1, 0, len(coordinates) - 1)
        score = 0
        for index in range(1, len(nums)):
            score = index * nums[index] + query(nums[index], 1, 0, len(coordinates) - 1)
            insert((-index, score), 1, 0, len(coordinates) - 1)
        return score
