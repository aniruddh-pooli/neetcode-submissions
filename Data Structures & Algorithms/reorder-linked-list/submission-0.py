class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        p1 = head
        p2 = head

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next

        right = p1.next
        p1.next = None
        left = head

        prev = None
        while right:
            nxt = right.next
            right.next = prev
            prev = right
            right = nxt

        right = prev

        while right:
            left_next = left.next
            right_next = right.next

            left.next = right
            right.next = left_next

            left = left_next
            right = right_next