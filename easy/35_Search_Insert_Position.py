class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search
        left =0
        right = len(nums)-1

        # iterating loop
        while left<=right:
            # find mid point
            mid=(left+right)//2
            # check mid point exists
            if nums[mid]==target:
                return mid 
            # update left/right properly
            if nums[mid]>target:
                right = mid-1

            else:
                left = mid+1
        return left

        