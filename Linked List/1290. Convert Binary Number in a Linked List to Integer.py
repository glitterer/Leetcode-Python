# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binNum = []
        while head is not None:
            binNum.append(head.val)
            head = head.next
        finalbin = "".join([f"{i}" for i in binNum])
        return int(finalbin, 2)
        
        
