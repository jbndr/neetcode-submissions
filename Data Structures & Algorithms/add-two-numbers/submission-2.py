# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [3, 5, 1]
# [7, 4]
# 153 + 47 = 200

# [0, 0, ]

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        head = ListNode()
        curr = head

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            s = a + b + carry
            carry = 1 if s >= 10 else 0
            s = s % 10

            curr.next = ListNode(val=s)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr.next = ListNode(val=1)

        return head.next

        