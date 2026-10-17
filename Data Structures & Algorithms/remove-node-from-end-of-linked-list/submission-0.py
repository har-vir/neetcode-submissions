# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = 1

        curr = head

        while curr:
            end += 1
            curr = curr.next

        target = end - n

        curr = head
        nex = None
        i = 1

        while curr:
            if target == 1:
                head = head.next
                break
            if i == target - 1:
                curr.next = curr.next.next if curr.next.next else None
            i += 1
            curr = curr.next

        return head
            

