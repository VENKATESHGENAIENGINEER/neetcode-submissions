class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=[]


        unique=sorted(list(set(nums)))
        print(unique)
       

        if len(unique)==0:
            return 0
        current_length=1
        max_length=1
        for i  in range(1,len(unique)):
            if unique[i]==unique[i-1]+1:
                current_length+=1
            else:
                max_length= max(current_length,max_length)
                current_length=1
        max_length= max(max_length,current_length)
        return max_length
            

