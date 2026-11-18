class Solution:
    def reverseKGroup(self, head, k):

        if head is None:
            return head

        current = head
        new_head = None
        tail = None

        while current is not None:

            group_head = current
            previous = None
            count = 0

            while current is not None and count < k:

                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
                count += 1

            if new_head is None:
                new_head = previous

            if tail is not None:
                tail.next = previous

            tail = group_head

        return new_head