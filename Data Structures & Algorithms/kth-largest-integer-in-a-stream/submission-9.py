class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        sorted_arr = sorted(nums)
        self.dq = deque(sorted_arr)
        
        while len(self.dq) > k:
            self.dq.popleft()

    def add(self, val: int) -> int:
        if len(self.dq) == 0:
            self.dq.append(val)
            return val

        if len(self.dq) < self.k:
            self.dq.append(val)
            self.dq = deque(sorted(self.dq))
            return self.dq[0]

        if val > self.dq[0]:
            self.dq.popleft()
            self.dq.append(val)
            self.dq = deque(sorted(self.dq))   # 🔥 FIX

        return self.dq[0]

 