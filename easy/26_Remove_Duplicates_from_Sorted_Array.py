class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # counter
        change_index = 1
        # iterating nums
        for num in range(1,len(nums)):
            # check repeated number in sorted list
            if nums[num]!=nums[num-1]:
                # update the list and increase the counter
                nums[change_index] = nums[num]
                change_index+=1
            
        return change_index
        