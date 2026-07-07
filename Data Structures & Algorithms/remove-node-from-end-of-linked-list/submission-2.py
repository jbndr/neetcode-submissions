# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # There is a solution without counting first

        # Keep to pointers of distance n
        # left ------ (n) ------ right
        # Move both pointers until right at end
        # left is now at the index that should be skipped
        if not head:
            return

        dummy = ListNode(val="-1", next=head)

        left = dummy
        right = head

        # [d,5]


        # move right n steps
        steps = n
        while steps > 0:
            right = right.next
            steps -= 1
        
        # now left and right have distance of n
        # move to the end:

        while right:
            right = right.next
            left = left.next

        # right at the end, left should skip the next val        
        left.next = left.next.next

        return dummy.next

