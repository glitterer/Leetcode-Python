# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = list()
        l2_list = list()
        while l1 is not None:
            l1_list.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            l2_list.append(l2.val)
            l2 = l2.next
        l1_list = ''.join(map(str, l1_list[::-1]))
        l2_list = ''.join(map(str, l2_list[::-1]))
        ans = []
        ans2 = []
        ans = int(l1_list) + int(l2_list)
        ans2 = [int(x) for x in str(ans)][::-1]

        
        # list to listNode 출처: https://stackoverflow.com/questions/57417731/converting-a-list-into-listnode
        head = ListNode(ans2[0])
        tail = head
        cnt = 1
        while cnt < len(ans2):
            print(head)
            tail.next = ListNode(ans2[cnt])
            tail = tail.next
            cnt+=1
        
        
        return head
