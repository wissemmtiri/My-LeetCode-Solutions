# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while None in lists:
            lists.remove(None)

        if not lists:
            return None

        head = ListNode()
        current = head
        while lists:
            min_node = lists[0]
            min_index = 0
            for i in range(1, len(lists)):
                if lists[i].val < min_node.val:
                    min_node = lists[i]
                    min_index = i
            current.next = min_node
            current = current.next
            lists[min_index] = lists[min_index].next
            if not lists[min_index]:
                lists.pop(min_index)

        return head.next