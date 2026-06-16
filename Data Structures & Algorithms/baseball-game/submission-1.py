class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for opr in operations:
            if opr == "+":
                new_record = int(stack[-1]) + int(stack[-2])
                stack.append(new_record)
                print(stack)
            elif opr == "C":
                stack.pop()
                print(stack)
            elif opr == "D":
                new_record = int(stack[-1]) * 2
                stack.append(new_record)
                print(stack)
            else:
                stack.append(opr)
                print(stack)
        total = 0
        for elem in stack:
            total += int(elem)
        return total