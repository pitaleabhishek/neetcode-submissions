# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find mid
        dummy1 = node1 = ListNode()
        dummy2 = node2 = ListNode()
        curr = head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        dummy2.next = slow.next
        slow.next = None
        dummy1.next = curr
        #reverse second
        prev, curr = None, dummy2.next
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        dummy2.next = prev
        #[2,4,6]
        #[8,10]
        dummy3 = node3 = ListNode()
        first = dummy1.next
        second = dummy2.next
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


        
        



        