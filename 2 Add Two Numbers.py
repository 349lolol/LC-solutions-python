# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(0, None)
        head = ret
        while(l1 is not None or l2 is not None):
            if l1 is not None:
                ret.val = ret.val + l1.val
                l1 = l1.next
            if l2 is not None:
                ret.val = ret.val + l2.val
                l2 = l2.next
            if ret.val >= 10: #carry
                ret.val = ret.val % 10
                ret.next = ListNode(1, None)
                ret = ret.next
            elif l1 is not None or l2 is not None:
                ret.next = ListNode(0, None)
                ret = ret.next
        
        return head

