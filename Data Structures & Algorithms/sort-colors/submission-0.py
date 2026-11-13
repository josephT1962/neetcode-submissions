class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        loc_0 =0
        loc_1 =0
        loc_2 =0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[loc_2]=2
                nums[loc_1]=1
                nums[loc_0]=0
                loc_0+=1
                loc_1+=1
                loc_2+=1
            elif nums[i]==1:
                nums[loc_2]=2
                nums[loc_1]=1                
                loc_1+=1
                loc_2+=1
            else:
                nums[loc_2]=2             
                loc_2+=1                
