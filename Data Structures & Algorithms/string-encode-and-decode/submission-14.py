class Solution:

    def encode(self, strs: List[str]) -> str:
        secreat_code="&venkat&"
        newword=""
        dummy ="&bal&"

        for i in range(len(strs)):
            if strs[i]=="":
                newword+=dummy+secreat_code
            else:
                newword+=strs[i]+secreat_code 
        return newword

    def decode(self, s: str) -> List[str]:
        secreat_code="&venkat&"
        dummy ="&bal&"

        if not s:
            return []

        new_list = s.split(secreat_code)
        if len(new_list)>0:
           new_list.pop()

        for i in range(len(new_list)):
            if new_list[i]==dummy:
                new_list[i]=""
        
        return new_list