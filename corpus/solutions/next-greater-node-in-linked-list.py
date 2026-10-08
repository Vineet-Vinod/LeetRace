class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values: list[int] = []
        node = head
        while node is not None:
            values.append(node.val)
            node = node.next
        answer = [0] * len(values)
        stack: list[int] = []
        for i, value in enumerate(values):
            while stack and values[stack[-1]] < value:
                answer[stack.pop()] = value
            stack.append(i)
        return answer
