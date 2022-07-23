# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        now = head
        
        while now != None:
            temp = now.next
            now.next = previous
            previous = now
            now = temp
            
        return previous
