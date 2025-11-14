class Solution:
    def numberOfSteps(self, num: int) -> int:
        def recursive_solution(num):
            # base case
            if num==0:
                return 0
            
            if num%2==0:
                return 1+ self.numberOfSteps(num//2)
            else:
                return 1+ self.numberOfSteps(num-1)
        
        #return recursive_solution(num) 
        

        # memorisation
        memo={}
        memo[0]=0
        def memorisation(num):
            if num in memo:
                return memo.get(num)
            if num%2==0:
                val = memorisation(num//2)+1
                memo[num]=val
                return memo.get(num)
            else:
                val = memorisation(num-1)+1
                memo[num]=val
                return memo.get(num)
        
        # tabularisation
        def tabularisation(num):
            memo=[0]*(num+1)
            for i in range(1,num+1):
                if i%2==0:
                    memo[i]=1+memo[i//2]
                else:
                    memo[i]=memo[i-1]+1
            return memo[num]
        #return tabularisation(num)
        return memorisation(num)

        