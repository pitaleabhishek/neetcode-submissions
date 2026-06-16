class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       
        zipped_ps = []

        time_stack = []
        for p,s in zip(position, speed):
            zipped_ps.append([p,s])
            
        sorted_zip = (sorted(zipped_ps, reverse=True))
        print(sorted_zip)

        for p, s in sorted_zip:
            time_taken = (target - p)/s
            time_stack.append(time_taken)
            if len(time_stack) >= 2 and time_stack[-1] <= time_stack[-2]:
                    time_stack.pop()
                    
        return len(time_stack)