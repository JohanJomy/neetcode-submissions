class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in '+-*/':
                a = stack.pop() 
                b = stack.pop()

                if i == '+':
                    b += a
                elif i == '-':
                    b -= a
                elif i == '*':
                    b *= a
                else:
                    b /= a

                stack.append(int(b))
            else:
                stack.append(int(i))

        return stack[0]