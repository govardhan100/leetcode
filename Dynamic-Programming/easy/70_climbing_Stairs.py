class Solution:
    def climbStairs(self, n: int) -> int:

        # recursive solution

        # def recursive_solution(n:int):
        #     if n==1 or n==2:
        #         return n
        #     return recursive_solution(n-1)+recursive_solution(n-2)
        # return recursive_solution(n)


        # # memorisation 
        # memo={}
        # memo[1]=1
        # memo[2]=2
        # def memorisation_solution(n:int):
        #     if n in memo:
        #         return memo.get(n)
        #     val = memorisation_solution(n-1)+memorisation_solution(n-2)
        #     memo[n]=val
        #     return val
        # return memorisation_solution(n)
                            

        # Tabulersation 

        # def tabular_solution(n):
        #     if n==1 or n==2:
        #         return n
        #     memo=[0]*(n+1)
        #     memo[1]=1
        #     memo[2]=2
        #     for i in range(3,n+1):
        #         memo[i]=memo[i-1]+memo[i-2]
        #     return memo[n]
        # return tabular_solution(n)
        
        # efficient solution

        def optimise_solution(n:int):
            if n==1 or n==2:
                return n
            last,second_last =2,1
            for i in range(3,n+1):
                last,second_last = last+second_last,last
            return last
        return optimise_solution(n)