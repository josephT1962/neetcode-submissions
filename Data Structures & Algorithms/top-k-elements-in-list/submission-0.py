class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_list ={}
        for i in range(len(nums)):
            if nums[i] in dict_list:
                dict_list[nums[i]]+=1
            else:
                dict_list[nums[i]]=1
        dict_list_sorted = sorted(dict_list.items(),key = lambda item: item[1], reverse = True)
        #print(dict_list_sorted)
        k_return =[]
        for j in range(k):
            k_return.append(dict_list_sorted[j][0])
        return k_return
