# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow_pointer = head.next
        fast_pointer = head.next.next if head.next else None

        while slow_pointer and fast_pointer:
            if slow_pointer == fast_pointer:
                return True

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next if fast_pointer.next else None

        return False
        