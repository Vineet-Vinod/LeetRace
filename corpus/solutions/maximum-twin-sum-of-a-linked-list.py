class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        size = len(values)
        return max(
            values[index] + values[size - index - 1] for index in range(size // 2)
        )
