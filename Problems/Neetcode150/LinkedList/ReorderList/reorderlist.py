# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        
        # find the middle point
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # second half is slow.next
        second = slow.next
        slow.next = None
        prev = None
        
        #reversing the second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
            
        # merge the two halves
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2