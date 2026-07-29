class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_Arr=[]
        for i in range(len(temperatures)):
            length=0
            found=False
            for j in range(i+1,len(temperatures)):                
                if temperatures[i]<temperatures[j]:
                    length+=1
                    found=True
                    break
                else:
                    length+=1
            if not found:
                length=0    
            result_Arr.append(length)
        return result_Arr