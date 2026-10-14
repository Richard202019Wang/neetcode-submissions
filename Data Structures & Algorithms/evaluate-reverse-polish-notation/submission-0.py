class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            elif token == "+":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 + num2)
            elif token == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif token == "*":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 * num1)
            elif token == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2 / num1))
        return stack[0]


        