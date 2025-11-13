class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        output =[0]
        count =0
        for i in nums:
            if i:
                count+=1
            else:
                count-=1
            output.append(count)
        
        max_cont=0
        memo={}
        for index,i in enumerate(output):
            if i in  memo:
                max_cont=max(index-memo.get(i),max_cont)
            else:
                memo[i]=index
        return max_cont

        