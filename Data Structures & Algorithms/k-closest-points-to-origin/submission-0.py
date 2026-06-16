class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from math import sqrt
        x1, y1 = 0, 0
        result = []
        final_res = []
        for x2,y2 in points:
            temp_dist = sqrt((x1 - x2)**2 + (y1 - y2)**2)
            result.append([temp_dist, x2, y2]) 
        result.sort()
        while len(result) > k:
            result.pop() 
        
        for x,y,z in result:
            final_res.append([int(y),int(z)])
        return (final_res)





