class Solution:
    def fib(self, n: int) -> int:
        ###########################
        # recursive method

        ###########################
        

        # def recursive_method(n):
        #     if n==0 or n==1:
        #         return n
            
        #     return recursive_method(n-1)+recursive_method(n-2)
        # return recursive_method(n)

        ###########################

        #  memorisation

        ###########################
        # memo={}
        # memo[0]=0
        # memo[1]=1
        # def memorisation_solution(n):
        #     if n in memo:
        #         return memo[n]
        #     val = memorisation_solution(n-1) +memorisation_solution(n-2)
        #     memo[n]=val
        #     return memo[n]
        # return memorisation_solution(n)
        
        # ###############################

            # Tabularisation 

        # #############################

        # def tabularisation(n):
        #     if n==0 or n==1:
        #         return n
        #     table= [0]*(n+1)
        #     table[1]=1

        #     for i in range(2,n+1):
        #         table[i]=table[i-1]+table[i-2]
        #     return table[n]
        # return tabularisation(n)


        # optimised solution

        def optimised_solution(n):
            if n==1 or n==0:
                return n
            n_1,n_2=1,0
            for i in range(2,n+1):
                n_1,n_2=n_1+n_2,n_1
            return n_1
        return optimised_solution(n)




        