class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # counter initialisation
        counter = 0
        # iterate the nums
        for index,num in enumerate(nums):
            # nums is val
            if num!=val:
                # update the list and counter
                nums[counter]= num
                counter+=1
        return counter
    
                
        