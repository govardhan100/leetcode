class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        ################################
            # Recursive Solution
        
        ################################


        # recursively

        # m =len(grid)-1
        # n = len(grid[0])-1
        # def recursively_solution(m,n):
        #     if m==0 and n==0:
        #         return grid[m][n]
            
        #     if m==0:
        #         return grid[m][n]+recursively_solution(m,n-1)
        #     if n==0:
        #         return grid[m][n]+recursively_solution(m-1,n)
        #     return grid[m][n]+ min(recursively_solution(m-1,n),recursively_solution(m,n-1))
        # return recursively_solution(m,n)

        # ################################
            
            # Memoirisation    
            
        # ################################

        # cache={}
        # cache[(0,0)]=grid[0][0]
        # m = len(grid)-1
        # n =len(grid[0])-1
        # def memorisation_solution(m,n):
        #     if (m,n) in cache:
        #         return cache[(m,n)]
        #     if m==0:
        #         val =memorisation_solution(m,n-1)+grid[m][n]
        #         cache[(m,n)]=val
        #         return cache[(m,n)]
        #     if n ==0:
        #         val= memorisation_solution(m-1,n)+grid[m][n]
        #         cache[(m,n)]=val
        #         return cache[(m,n)]
        #     val =grid[m][n]+min(memorisation_solution(m-1,n),memorisation_solution(m,n-1))

        #     cache[(m,n)]=val
        #     #print(m,n,val)
        #     return cache[(m,n)]
        
        # return memorisation_solution(m,n)

        # ###################################
            
                    # Tabular Method 

        # ###################################


        def Tabular_Method():

            memo=[[0]*len(grid[0]) for i in grid]
            
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if i==0 and j==0:
                        memo[i][j]=grid[0][0]
                        continue
                    if i==0:
                        memo[i][j]=grid[i][j]+memo[i][j-1]
                        continue
                    if j ==0:
                        memo[i][j]=grid[i][j]+memo[i-1][j]
                        continue
                    memo[i][j]=grid[i][j]+ min(memo[i-1][j],memo[i][j-1])
            
            return memo[len(grid)-1][len(grid[0])-1]

        return Tabular_Method()