class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        rev = head

        if head.next:
            rev = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return rev
