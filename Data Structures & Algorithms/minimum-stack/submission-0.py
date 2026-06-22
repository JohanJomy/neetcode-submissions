class MinStack:

    def __init__(self):
        self.stack = []
        self.prefixmin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.prefixmin:
            self.prefixmin.append(val)
        else:
            self.prefixmin.append(min(val, self.prefixmin[-1]))



    def pop(self) -> None:
        self.stack.pop()
        self.prefixmin.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefixmin[-1]
