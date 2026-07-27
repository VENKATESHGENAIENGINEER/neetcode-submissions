class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp_list=""
        for i in s:
            if i.isalnum():
                tmp_list+=i.lower()
                
           
        return tmp_list==tmp_list[::-1]



