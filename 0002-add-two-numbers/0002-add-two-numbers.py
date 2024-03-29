# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recursive(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry
            newNode = ListNode(sum % 10)
            newNode.next = recursive(l1.next if l1 else None, l2.next if l2 else None, sum // 10)
            return newNode
        return recursive(l1, l2, 0)