class Solution:
    def handleQuery(
        self, nums1: List[int], nums2: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(nums1)
        tree = [0] * (4 * n)
        lazy = [False] * (4 * n)

        def build(node, lo, hi):
            if lo == hi:
                tree[node] = nums1[lo]
            else:
                mid = (lo + hi) // 2
                build(node * 2, lo, mid)
                build(node * 2 + 1, mid + 1, hi)
                tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def flip(node, lo, hi):
            tree[node] = hi - lo + 1 - tree[node]
            lazy[node] = not lazy[node]

        def update(node, lo, hi, left, right):
            if left <= lo and hi <= right:
                flip(node, lo, hi)
                return
            mid = (lo + hi) // 2
            if lazy[node]:
                flip(node * 2, lo, mid)
                flip(node * 2 + 1, mid + 1, hi)
                lazy[node] = False
            if left <= mid:
                update(node * 2, lo, mid, left, right)
            if right > mid:
                update(node * 2 + 1, mid + 1, hi, left, right)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        build(1, 0, n - 1)
        total = sum(nums2)
        answer = []
        for kind, a, b in queries:
            if kind == 1:
                update(1, 0, n - 1, a, b)
            elif kind == 2:
                total += a * tree[1]
            else:
                answer.append(total)
        return answer
