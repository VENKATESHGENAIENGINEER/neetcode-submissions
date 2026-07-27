class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr=[]
        for i in range(len(nums)):
            tmp_arr=nums

            result_product=1
            if len(tmp_arr)>0:
                k=0
                while k<len(tmp_arr):
                    if k != i:
                        result_product*=tmp_arr[k]
                    k+=1

            result_arr.append(result_product)
        return result_arr