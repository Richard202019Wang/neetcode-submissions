# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result, new_head = None, None
        while list1 or list2:
            if not new_head:
                if list1 and list2:
                    if list1.val > list2.val:
                        new_head = list2
                        list2 = list2.next
                    else:
                        new_head = list1
                        list1 = list1.next
                elif list1 and not list2:
                    new_head = list1
                    list1 = list1.next
                elif list2 and not list1:
                    new_head = list2
                    list2 = list2.next
                else:
                    return None
                result = new_head
            else:
                if list1 and list2:
                    if list1.val > list2.val:
                        new_head.next = list2
                        list2 = list2.next
                    else:
                        new_head.next = list1
                        list1 = list1.next
                elif list1 and not list2:
                    new_head.next = list1
                    list1 = list1.next
                elif list2 and not list1:
                    new_head.next = list2
                    list2 = list2.next
                new_head = new_head.next
        return result