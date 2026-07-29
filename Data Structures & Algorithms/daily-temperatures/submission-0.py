class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result_Arr=[]
        print(len(temperatures))
        for i in range(len(temperatures)):
            length=0
            found=False
            for j in range(i+1,len(temperatures)):
                print(i,j)
                print(temperatures[i],temperatures[j])
                
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