class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear_list = set()
        for i in range(len(nums)):
            temp_i= nums[i]
            if temp_i in appear_list:
                    return True
            else:
                appear_list.add(temp_i)
        return False