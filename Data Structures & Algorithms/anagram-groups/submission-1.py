class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_arr=[]


        for i in range(len(strs)):
            present_arr=[]

            for j in range(len(strs)):
                if sorted(strs[i])==sorted(strs[j]):

                    present_arr.append(strs[j])
            if present_arr in result_arr:
                continue
            else:
                result_arr.append(present_arr)
        

        return result_arr


