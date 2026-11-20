class Solution:
    def countNodesInLoop(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                count = 1
                current = slow.next

                while current != slow:
                    count += 1
                    current = current.next

                return count

        return 0