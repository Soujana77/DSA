class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        previous = None
        current = slow

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        left = head
        right = previous

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True