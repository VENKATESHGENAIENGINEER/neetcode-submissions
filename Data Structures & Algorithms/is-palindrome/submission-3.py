class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp_list=""
        for i in range(len(s)):
            print(s[i])
            if s[i] == " " or not s[i].isalnum():
                pass
            else:
                tmp_list+=s[i].lower()
                
           
        return tmp_list==tmp_list[::-1]



