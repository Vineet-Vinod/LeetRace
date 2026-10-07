class Solution:
    def nextGreaterElement(self, n: int) -> int:
        a = list(str(n))
        i = len(a) - 2
        while i >= 0 and a[i] >= a[i + 1]:
            i -= 1
        if i < 0:
            return -1
        j = len(a) - 1
        while a[j] <= a[i]:
            j -= 1
        a[i], a[j] = a[j], a[i]
        a[i + 1 :] = reversed(a[i + 1 :])
        ans = int("".join(a))
        return ans if ans < 2**31 else -1
