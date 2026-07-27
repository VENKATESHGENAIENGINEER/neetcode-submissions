class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_dict=dict()
        print(nums)
        for i in range(len(nums)):
            print(nums[i])
            if result_dict.get(nums[i])is not None and result_dict.get(nums[i])>=1:
                result_dict[nums[i]]=result_dict.get(nums[i])+1

            else:
                result_dict[nums[i]]=1
        #find top k elements which repeated most time
        print(result_dict)
        sorted_items=sorted(result_dict.items(), key=lambda item:item[1],reverse=True)
        print(sorted_items)
        topk=sorted_items[:k]
        return [i[0] for i in topk]

        