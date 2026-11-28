from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0

        queue = deque([(root, 0)])
        maximum_width = 0

        while queue:
            size = len(queue)
            first = queue[0][1]
            last = queue[-1][1]

            maximum_width = max(maximum_width, last - first + 1)

            for _ in range(size):
                node, index = queue.popleft()
                index -= first

                if node.left:
                    queue.append((node.left, 2 * index))

                if node.right:
                    queue.append((node.right, 2 * index + 1))

        return maximum_width