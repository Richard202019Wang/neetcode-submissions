# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_len, l2_len = 0, 0
        result = 0
        while l1.next:
            result += 10 ** l1_len * l1.val
            l1 = l1.next
            l1_len += 1
        result += 10 ** l1_len * l1.val

        while l2.next:
            result += 10 ** l2_len * l2.val
            l2 = l2.next
            l2_len += 1
        result += 10 ** l2_len * l2.val

        current = result % 10
        result //= 10
        prev_node = ListNode(current, None)
        dummy = ListNode(None, prev_node)
        while result // 10:
            cur = result % 10
            result //= 10
            cur_node = ListNode(cur, None)
            prev_node.next = cur_node
            prev_node = cur_node
        if result != 0:
            last_node = ListNode(result, None)
            prev_node.next = last_node
        return dummy.next

        