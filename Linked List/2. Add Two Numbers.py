# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummyhead = ans
        ans_temp = 0
        digit_carry = 0
        while l1 is not None or l2 is not None: 
            if l1 is None:
                ans_temp = 0 + l2.val + digit_carry
                l2 = l2.next
            elif l2 is None:
                ans_temp = l1.val + 0 + digit_carry
                l1 = l1.next
            else:
                ans_temp = l1.val + l2.val + digit_carry
                l1 = l1.next
                l2 = l2.next
            digit_carry = 0
            if ans_temp >= 10:
                digit_carry = 1
                ans_temp -= 10
            ans.val = ans_temp
            
            if l1 is None and l2 is None and digit_carry == 1:
                ans.next = ListNode()
                ans.next.val = 1
                return dummyhead
            
            if l1 is not None or l2 is not None:
                ans.next = ListNode()
                ans = ans.next
        return dummyhead
        # return dummyhead.next 로 바꿔봅시다..!
