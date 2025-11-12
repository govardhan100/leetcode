class Solution:
    def tribonacci(self, n: int) -> int:

        #  ################

        # recursive 

        ###########

        def recursive(n):
            if n==0 or n==1:
                return n
            if n==2:
                return 1
            return recursive(n-1) + recursive(n-2)+recursive(n-3)


        # ##########

        # memorisation

        #############
        memo={}

        def memorisation(n):
            if n in memo:
                return memo[n]
            
            if n==0 or n==1:
                memo[n]=n
                return memo[n]
            
            if n==2:
                memo[n]=1
                return memo[n]
            
            memo[n] = memorisation(n-1)+memorisation(n-2)+memorisation(n-3)
            return memo[n]
        
        #return memorisation(n)
            
        # #######################


        # Tabularisation

        #########################
        def tabularisation(n):
            if n==0 or n==1:
                return n
            if n==2:
                return 1
            # initialisation
            memo=[0]*(n+1)
            memo[1]=1
            memo[2]=1
            for i in range(3,n+1):
                memo[i]=memo[i-1]+memo[i-2]+memo[i-3]
            return memo[n]
        #return tabularisation(n)

        # optimisated solution
        def optimisation(n):
            if n==0 or n==1:
                return n
            if n==2:
                return 1
            last,second_last,third_last =1,1,0
            for i in range(3,n+1):
                last,second_last,third_last=last+second_last+third_last,last,second_last
            return last
        
        return optimisation(n)
            