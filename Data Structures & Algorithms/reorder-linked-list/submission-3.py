# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        nodes = []

        while head:
            nodes.append(head)
            head = head.next
        
        a = 1
        b = len(nodes) - 1
        switch = 1

        head = nodes[0]
        curr = head

        while a <= b:
            if switch == 1:
                curr.next = nodes[b]
                b -= 1
                switch = 0
            else:
                curr.next = nodes[a]
                a += 1
                switch = 1
            curr = curr.next
            
        curr.next = None
        return None
            