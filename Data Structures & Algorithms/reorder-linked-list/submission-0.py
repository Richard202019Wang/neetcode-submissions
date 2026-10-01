# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid_head = slow.next
        prev = None
        slow.next = None
        while mid_head:
            temp = mid_head.next
            mid_head.next = prev
            prev = mid_head
            mid_head = temp
        
        first, sec = head, prev
        while sec:
            temp1, temp2 = first.next, sec.next
            first.next = sec
            sec.next = temp1
            first, sec = temp1, temp2


        