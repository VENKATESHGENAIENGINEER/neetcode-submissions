class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            visited=target-nums[i]
            if visited in seen:
                return[seen[visited],i]
            seen[nums[i]]=i
        