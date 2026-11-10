class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_num = {}
        for i in nums:
            if i not in dict_num:
                dict_num[i]=1
            else:
                dict_num[i]+=1

        for key,value in dict_num.items():
            if value>=len(nums)//2:
                return key
        #return max(dict_num,key=dict_num.get)