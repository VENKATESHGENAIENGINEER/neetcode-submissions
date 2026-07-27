class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict=dict()
        t_dict=dict()
        for i in s:
            if s_dict.get(i)==1:
                s_dict[i] = s_dict.get(i)+1
            else:
                s_dict[i]=1
        for j in t:
            if  t_dict.get(j)==1:
                t_dict[j]= t_dict.get(j)+1
            else:
                t_dict[j]=1
        s_dict= dict(sorted(s_dict.items()))
        t_dict= dict(sorted(t_dict.items()))
        if s_dict==t_dict:
            return True
        else:
            return False
