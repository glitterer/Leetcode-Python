# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        finder_head = head
        middle_head = head
        while finder_head is not None:
            cnt += 1
            finder_head = finder_head.next
        for i in range(cnt//2):
            middle_head = middle_head.next
        while middle_head is not None:
            return middle_head
