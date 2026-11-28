class Solution:
    def isValidBST(self, root):

        def validate(node, minimum, maximum):
            if not node:
                return True

            if not minimum < node.val < maximum:
                return False

            return (
                validate(node.left, minimum, node.val)
                and
                validate(node.right, node.val, maximum)
            )

        return validate(root, float('-inf'), float('inf'))