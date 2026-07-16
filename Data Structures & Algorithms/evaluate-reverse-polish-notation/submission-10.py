class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            print(token)
            if token in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a+b)
                if token == "-":
                    stack.append(a-b)
                if token == "*":
                    stack.append(a*b)
                if token == "/":
                    if b == 0:
                        stack.append(0)
                    else:
                        stack.append(int(a/b))
            else:
                stack.append(float(token))
            
            print(stack)

        return int(stack[-1])