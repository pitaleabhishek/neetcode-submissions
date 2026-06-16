class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for n in nums:
            heapq.heappush(heap, -n)

        while k > 0:
            kth_largest = -heapq.heappop(heap)
            k -= 1

        return kth_largest
        