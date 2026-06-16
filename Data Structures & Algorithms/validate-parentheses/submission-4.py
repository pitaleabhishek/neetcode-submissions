class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {"]":"[", "}":"{", ")":"("}

        for char in s:
            if char in "[{(":
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() != dict1[char]:
                    return False
        return len(stack) == 0
