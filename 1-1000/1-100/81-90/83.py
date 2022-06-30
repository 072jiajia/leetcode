from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = new_list_last = ListNode(None)
        while head is not None:
            if head.val != new_list_last.val:
                new_list_last.next = ListNode(head.val)
                new_list_last = new_list_last.next
            head = head.next
        return new_list.next
