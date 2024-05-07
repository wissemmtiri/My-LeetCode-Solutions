# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def backwardPropagate(node: ListNode):
            if node is None:
                return 0
            carry = backwardPropagate(node.next)
            total = node.val * 2 + carry
            node.val = total % 10
            return total // 10

        carry = backwardPropagate(head)
        if carry:
            return ListNode(carry, head)
        return head