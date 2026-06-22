class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in '+-*/':
                a = stack.pop() 
                b = stack.pop()

                if i == '+':
                    res = b + a
                elif i == '-':
                    res = b - a
                elif i == '*':
                    res = b * a
                else:
                    res = b / a

                stack.append(int(res))
            else:
                stack.append(int(i))

        return stack[0]