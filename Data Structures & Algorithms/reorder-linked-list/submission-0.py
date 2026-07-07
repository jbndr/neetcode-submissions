# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def printList(self, head):
        if not head:
            print("List empty")

        res = []
        curr = head
        while curr:
            res.append(str(curr.val))
            curr = curr.next

        print(",".join(res))

    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = head
        fast = head.next if head else None

        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None

        mid = slow

        prev = None
        curr = slow

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        first = head.next
        second = prev

        start = head

        self.printList(head)
        self.printList(first)
        self.printList(second)

        i = 1

        while second and start:
            if i % 2 == 0:
                start.next = first
                first = first.next if first else None
            else:
                start.next = second
                second = second.next
            start = start.next
            i += 1


        

        
        





        


        