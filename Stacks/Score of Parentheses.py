class Solution:
    def scoreOfParentheses(self, s):
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)

            else:
                value = stack.pop()
                score = max(2 * value, 1)
                stack[-1] += score

        return stack[0]