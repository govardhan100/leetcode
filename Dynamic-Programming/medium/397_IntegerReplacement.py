class Solution:
    def integerReplacement(self, n: int) -> int:
        # recursive solution

        def recursive_solution(n):
            if n==1:
                return 0
            if n%2==0:
                return 1+ self.integerReplacement(n//2)
            else:
                return 1+ min(self.integerReplacement(n-1),self.integerReplacement(n+1))
        #return recursive_solution(n)

        # memorisation
        memo={}
        memo[1]=0

        def memorisation_solution(n):
            if n in memo:
                return memo.get(n)
            if n%2==0:
                val = 1+memorisation_solution(n//2)
                memo[n]=val
                return memo.get(n)
            else:
                val= 1+min(memorisation_solution(n-1),memorisation_solution(n+1))
                memo[n]=val
                return memo.get(n)

        #return memorisation_solution(n)

        def tabularisation(n):
            
            # We need dp up to n+1 in case we use (i+1)
            dp = [0] * (n + 2)

            dp[1] = 0     # base case
            dp[2] = 1     # 2 → 1 by 1 step

            for i in range(3, n + 1):
                if i % 2 == 0:
                    dp[i] = 1 + dp[i // 2]
                else:
                    dp[i] = min(
                        1 + dp[i - 1],           # subtract 1
                        2 + dp[(i + 1) // 2]     # add 1, then divide
                    )

            return dp[n]
        #return tabularisation(n)
        return  memorisation_solution(n) 
