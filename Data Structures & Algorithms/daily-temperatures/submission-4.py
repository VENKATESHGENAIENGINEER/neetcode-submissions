class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List:
        n =len(temperatures)

        result_Arr=[0]*n
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev_index=stack.pop()
                result_Arr[prev_index]=i-prev_index
            stack.append(i)
        return result_Arr


        