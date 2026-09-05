# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        greater = ListNode(0)

        left = less
        right = greater

        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            head = head.next

        # Connect both lists
        left.next = greater.next

        # End the greater list
        right.next = None

        return less.next