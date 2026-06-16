# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy1 = node1 = ListNode()
        dummy2 = node2 = ListNode()
        curr = head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        dummy2.next = slow.next #[8,10,N]
        slow.next = None 
        dummy1.next = curr #[2,4,6,N]

        prev, curr = None, dummy2.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        dummy2.next = prev
        first, second = dummy1.next, dummy2.next
        dummy3 = node3 = ListNode()

        while first and second:
            node3.next = first
            first = first.next
            node3 = node3.next

            node3.next = second
            second = second.next
            node3 = node3.next

        if first:
            node3.next = first

        head = dummy3.next





        
