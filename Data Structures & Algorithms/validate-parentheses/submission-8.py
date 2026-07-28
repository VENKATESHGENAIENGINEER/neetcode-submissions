class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        open_strings=["{","[","("]
        close_strings=["}","]",")"]
        for i in s:
            if i in open_strings:
                stack.append(i)
            elif i not in open_strings:
                if len(stack)<1:
                    return False
                val=stack[-1]
                if i == "}" and val !="{":
                    return False
                elif i == "]" and val !="[":
                    return False
                elif i ==")" and val !="(":
                    return False
                stack.pop(-1)
        if len(stack)>1:
            if s[0] in open_strings and s[-1] not in close_strings:
                return False
            if 2*len(stack)==len(s):       
                return False
        return True

        