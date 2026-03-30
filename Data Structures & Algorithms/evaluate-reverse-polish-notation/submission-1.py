class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operator_set = set(["+", "-", "*", "/"])
    

        for token in tokens:
            if not token in operator_set:
                stack.append(token)
            else:
                second_num = int(stack.pop())
                first_num = int(stack.pop())
                if token == "+":
                    stack.append(first_num + second_num)
                elif token == "-":
                    stack.append(first_num - second_num)
                elif token == "*":
                    stack.append(first_num * second_num)
                elif token == "/":
                    stack.append(first_num / second_num)

        return int(stack[0])