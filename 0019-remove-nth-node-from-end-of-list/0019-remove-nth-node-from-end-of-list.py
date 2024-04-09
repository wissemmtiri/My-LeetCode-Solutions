# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def getLength(node: ListNode) -> int:
            length = 0
            while node:
                length += 1
                node = node.next
            return length
    
        length = getLength(head)
        dummy = ListNode(0, head)
        node = dummy

        for _ in range(length-n):
            node = node.next
        node.next = node.next.next

        return dummy.next