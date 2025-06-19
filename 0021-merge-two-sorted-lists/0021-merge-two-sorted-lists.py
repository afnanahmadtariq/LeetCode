# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        current, second = (list1, list2) if list1.val < list2.val else (list2, list1)
        head = current
        while current.next and second:
            if current.next.val > second.val:
                temp = current.next
                current.next = second
                second = temp
            current = current.next
        current.next = second
        return head
