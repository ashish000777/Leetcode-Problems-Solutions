# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        vec = []

        # Merge the two lists
        while list1:
            vec.append(list1.val)
            list1 = list1.next

        while list2:
            vec.append(list2.val)
            list2 = list2.next

        vec.sort()

        temp = ListNode(-1)
        head = temp
        for value in vec:
            temp.next = ListNode(value)
            temp = temp.next

        head = head.next
        return head
