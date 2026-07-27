class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value1=set(nums)
        if len(nums)!=len(value1):
            return True
        else:
            return False
        