# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        original = []
        reverse = []
        while head is not None:
            original.append(head.val)
            head = head.next
        reverse = original[::-1]
        return original == reverse
    
    
    #Facebook wanted a constant space solution == O(1) space complexity
