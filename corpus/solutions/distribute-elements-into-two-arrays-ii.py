class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        ranks = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
        size = len(ranks)
        trees = [[0] * (size + 1), [0] * (size + 1)]
        arrays = [[], []]

        def prefix(tree, index):
            total = 0
            while index:
                total += tree[index]
                index -= index & -index
            return total

        for i, v in enumerate(nums):
            r = ranks[v]
            if i < 2:
                chosen = i
            else:
                counts = [len(arrays[j]) - prefix(trees[j], r) for j in range(2)]
                chosen = (
                    0
                    if (counts[0], -len(arrays[0])) >= (counts[1], -len(arrays[1]))
                    else 1
                )
            arrays[chosen].append(v)
            while r <= size:
                trees[chosen][r] += 1
                r += r & -r
        return arrays[0] + arrays[1]
