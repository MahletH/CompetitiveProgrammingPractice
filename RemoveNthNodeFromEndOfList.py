# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        start=head
        end=head
        for i in range(n):
            end=end.next
        if not end:
            return start.next
        while end.next:
            start=start.next
            end=end.next         
        start.next=start.next.next
        return head
