class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return_list = [nums[0]]
        prev=nums[0]
        prev_loc=0
        for i in range(1,len(nums)):


            if nums[i]<=prev:
                # If no smaller/equal number is found, insert at the start.
                insert_loc = 0                            
                for j in range(prev_loc,-1,-1):
                    if nums[i]>= return_list[j]:
                        insert_loc = j + 1
                        break


            elif nums[i]>prev:
                # If no larger number is found, insert at the end.
                insert_loc = len(return_list)                
                for j in range(prev_loc+1,len(return_list)):
                    if nums[i]< return_list[j]:
                        insert_loc = j
                        break
            return_list = (
                return_list[:insert_loc]
                + [nums[i]]
                + return_list[insert_loc:]
            )

            prev = nums[i]
            prev_loc = insert_loc
        return return_list       