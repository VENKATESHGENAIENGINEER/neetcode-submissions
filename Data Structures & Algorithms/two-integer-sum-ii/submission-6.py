class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
  
        for i in range(n):
            for j in range(i,n):
                    
                
                if numbers[i]+numbers[j]==target:
                    if numbers[i]==numbers[j]:
                        return [i+1,j+1+1]
                    
                    return [i+1,j+1]
        return []
                    

        