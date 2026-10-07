class Solution:
    def numComponents(self, head: Optional[ListNode], nums: list[int]) -> int:
        selected = set(nums)
        components = 0
        inside = False
        while head is not None:
            if head.val in selected:
                if not inside:
                    components += 1
                inside = True
            else:
                inside = False
            head = head.next
        return components
