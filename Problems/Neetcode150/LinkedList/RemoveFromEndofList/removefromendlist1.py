# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
            

    def removeNthFromEnd(self, head, n):
        if not head.next and n == 1:
            return None
        
        rev = self.reverseList(head)
            
        count = 0
        copy = rev
        while count < n-2:
            rev = rev.next
            count += 1
        if n == 1:
            copy = copy.next
        else:
            rev.next = rev.next.next
        
        ans = self.reverseList(copy)
        
        return ans
            
            