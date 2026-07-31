class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n= len(heights)
        area = 0
        if n<=1:
            return 0
        for i in range(n):
            for j in range(i,n):
                result= min(heights[i], heights[j]) * (j - i)
                area=max(area,result)
                   
        return area

        