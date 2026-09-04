class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_set=set(nums)
        if len(distinct_set)==len(nums):
            return False
        else:
            return True
        
        