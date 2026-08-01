class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        print(n)
        area=0
        l_height=[]
        r_height=[]
        # first im trying brute force then in next attempt i will try 2 pointer techinque
        if n<1:
            return 0
        if n<2:
            l_height.append(height[0])
            r_height.append(height[-1])
      
        l_height.append(height[0])
        r_height = r_height[::-1]        
        for i in range(1,n):
            val= max(height[:i+1])
            l_height.append(val)
        for j in range(n-1,-1,-1):
            print(j)
            val= max(height[j:])
            r_height.append(val)
        print(l_height)
        print(r_height)
        r_height=r_height[::-1]
        

        for i in range(n):
            result= min(l_height[i],r_height[i])-height[i]
            #print(result)
            area += result

        return area



            

                


        