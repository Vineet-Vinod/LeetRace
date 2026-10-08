class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        positions = []
        index = 1
        previous = head
        current = head.next if head else None
        while current is not None and current.next is not None:
            if (current.val > previous.val and current.val > current.next.val) or (
                current.val < previous.val and current.val < current.next.val
            ):
                positions.append(index)
            previous = current
            current = current.next
            index += 1
        if len(positions) < 2:
            return [-1, -1]
        minimum = min(b - a for a, b in zip(positions, positions[1:]))
        return [minimum, positions[-1] - positions[0]]
