class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = []
        stack = []
        for p, s in sorted(zip(position, speed), reverse=True):
            pairs.append([p,s])

        for p, s in pairs:
            t = (target-p)/s

            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        
        