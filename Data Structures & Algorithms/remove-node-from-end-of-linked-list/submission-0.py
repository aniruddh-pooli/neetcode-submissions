class Solution:
    def removeNthFromEnd(self, head, n):

        # Reverse the list
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head = prev

        # Remove nth node from the beginning
        if n == 1:
            head = head.next
        else:
            curr = head
            for _ in range(n - 2):
                curr = curr.next
            curr.next = curr.next.next

        # Reverse the list again
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev