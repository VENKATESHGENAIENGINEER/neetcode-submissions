class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp_list=""
        for i in range(len(s)):
            print(s[i])
            if s[i] == " " or not s[i].isalnum():
                pass
            else:
                tmp_list+=s[i]
                
           
        #tmp_list=remove_special_char(tmp_list)
        tmp_list1=tmp_list[::-1]
        print(tmp_list1)
        if tmp_list1.lower() == tmp_list.lower():
            return True
        else:
            return False

        return True

def remove_special_char(string:str):
    newstr =""
    for i in range(len(string)):
        if string[i].isalnum():
            newstr+=string[i]
    print(newstr)
    return newstr

