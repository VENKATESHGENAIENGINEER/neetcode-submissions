class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_Arr=[]
        for i in range(len(temperatures)):
            length=0
            for j in range(i+1,len(temperatures)):  
                length+=1
                if temperatures[i]<temperatures[j]:
                    result_Arr.append(length)
                    break
            else:
                result_Arr.append(0)
        return result_Arr