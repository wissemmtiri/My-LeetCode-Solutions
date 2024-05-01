# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(node: ListNode, nextNode: ListNode):
            if not nextNode:
                return node
            tmp = nextNode.next
            nextNode.next = node
            node.next = swap(tmp, tmp.next) if tmp else None
            return nextNode
        return swap(head, head.next) if head and head.next else head