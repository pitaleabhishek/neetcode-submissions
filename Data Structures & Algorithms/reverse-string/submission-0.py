class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = 0
        while n < len(s):
            s.insert(n, s.pop())
            n += 1
            