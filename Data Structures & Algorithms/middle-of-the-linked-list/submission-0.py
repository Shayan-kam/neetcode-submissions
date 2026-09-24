# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head
        while tail.next != None:
            tail = tail.next
        slow = head
        fast = head
        while fast != tail:
            fast = fast.next.next
            slow = slow.next
            if fast == None:
                return slow
        return slow
        



        