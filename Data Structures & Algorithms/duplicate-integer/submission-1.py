class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for n in nums:
            if n not in set1:
                set1.add(n)
            else:
                return True
        return False
        