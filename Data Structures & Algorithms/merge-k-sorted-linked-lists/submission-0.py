# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)

        curr = dummy

        while True:
            min_val = float("inf")
            min_index = None

            for idx, pointer in enumerate(lists):
                if pointer and pointer.val < min_val:
                    min_val = pointer.val
                    min_index = idx

            if min_index is not None: # 0 evalutes to False
                curr.next = lists[min_index]
                curr = curr.next
                lists[min_index] = lists[min_index].next
            else:
                curr.next = None
                break

        return dummy.next

        