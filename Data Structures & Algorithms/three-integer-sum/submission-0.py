class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        target = 0
        result_arr=[]
        if n<3:
            return []
        for i in range(n):
          for j in range(i,n):
            for k in range(j,n):
                if i!=j!=k:
                    a,b,c = nums[i],nums[j],nums[k]
                    if a+b+c==target:
                        list1=sorted([a,b,c])
                        if list1 not in result_arr:
                             result_arr.append(list1)
        return result_arr

          