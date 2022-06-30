class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = root = ListNode()
        while True:
            if l1 is None:
                current.val += l2.val
                if l2.next is None:
                    break
                l2 = l2.next
            elif l2 is None:
                current.val += l1.val
                if l1.next is None:
                    break
                l1 = l1.next
            else:
                current.val += l1.val + l2.val
                if l1.next is None and l2.next is None:
                    break
                l1 = l1.next
                l2 = l2.next

            if current.val > 9:
                current.val -= 10
                current.next = ListNode(1)
            else:
                current.next = ListNode(0)
            current = current.next 

        if current.val > 9:
            current.val -= 10
            current.next = ListNode(1)
        
        return root
