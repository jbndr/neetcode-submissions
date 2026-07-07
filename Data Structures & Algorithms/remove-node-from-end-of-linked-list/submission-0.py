# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        length = 0

        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        target_index = length - n

        index = 0

        prev = None
        curr = head

        while curr:
            if index == target_index:
                # remove node
                if not prev:
                    head = curr.next
                else:
                    prev.next = curr.next
            index += 1
            prev = curr
            curr = curr.next

        return head
        
        

        