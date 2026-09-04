class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s):
            return False
        s_dict=dict()
        t_dict=dict()
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]]+=1
            else:
                 s_dict[s[i]]=1

            if t[i] in t_dict:
                t_dict[t[i]]+=1
            else:
                 t_dict[t[i]]=1
        print(s_dict)
        print(t_dict)
        if s_dict==t_dict:
            return True
        return False

