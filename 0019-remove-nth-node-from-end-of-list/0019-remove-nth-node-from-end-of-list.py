# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 1->2->3->4->5
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        N = 0
        while curr:
            N+=1
            curr = curr.next
        
        removeIndex = N-n
        if removeIndex == 0:
            return head.next
        
        curr = head
        for i in range(0, N-1):
            if (i+1) == removeIndex:
                curr.next = curr.next.next
            curr = curr.next
        return head

        
            
        