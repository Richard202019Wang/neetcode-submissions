# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # cur -> None(end) prev -> last node = reverse head
        cur_idx = 1
        while prev:      
            temp = prev.next
            if cur_idx == n:
                if temp:
                    prev = temp.next
                    temp.next = cur
                    cur = temp
                else:
                    prev = None
                    
            else:
                prev.next = cur
                cur = prev
                prev = temp
            cur_idx += 1
        return cur

            
        

        