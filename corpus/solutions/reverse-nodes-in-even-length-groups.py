class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_group_end = head
        group_size = 2
        while previous_group_end is not None:
            group_start = previous_group_end.next
            if group_start is None:
                break
            group_end = group_start
            actual_size = 1
            while actual_size < group_size and group_end.next is not None:
                group_end = group_end.next
                actual_size += 1
            after_group = group_end.next
            if actual_size % 2 == 0:
                old_start = group_start
                previous = after_group
                current = group_start
                while current is not after_group:
                    following = current.next
                    current.next = previous
                    previous = current
                    current = following
                previous_group_end.next = group_end
                previous_group_end = old_start
            else:
                previous_group_end = group_end
            group_size += 1
        return head
