class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # creating dict
        hashing_dict = {}

        # iterating list
        for index,num in enumerate(nums):
            # complement of sum
            complement = target - num

            # searching complement in dict
            if complement in hashing_dict:
                return [hashing_dict[complement],index]
            # adding if not find in the dict
            hashing_dict[num]=index
        