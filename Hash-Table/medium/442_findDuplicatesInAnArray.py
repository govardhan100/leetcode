class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # HashTable
        def hashtable_solution(nums):
            memo=set()
            output=[]
            for num in nums:
                if num in memo:
                    output.append(num)
                else:
                    memo.add(num)
            return output
        #return hashtable_solution(nums)
        def signingsame(nums):

            memo=[]
            # Marking 
            for i in nums:
                index=abs(i)-1
                if nums[index]<0:
                    memo.append(abs(i))
                else:
                    nums[index]=-nums[index]
            return memo
        return signingsame(nums)