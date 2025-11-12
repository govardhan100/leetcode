class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # ##############################

        # -------Tabularistion------

        # ##############################

        if len(obstacleGrid)==1 and len(obstacleGrid[0])==1:
            if obstacleGrid[0][0]:
                return 0
            return 1

        memo=[[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        
        memo[0][0]=0 if obstacleGrid[0][0]==1 else 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i==0 and j==0:
                    continue
                if obstacleGrid[i][j]==1:
                    memo[i][j]=0
                    continue
                if i==0:
                    memo[i][j]=memo[i][j-1]
                    continue
                if j==0:
                    memo[i][j]=memo[i-1][j]
                    continue
                memo[i][j]= memo[i-1][j]+memo[i][j-1]
        #print(memo)
        return memo[-1][-1]

        # ##############################
                
        # -------Memorisation------

        ################################

        #cache={(0,0): 0 if obstacleGrid[0][0] else 1}
        # m =len(obstacleGrid)-1
        # n = len(obstacleGrid[0])-1
        # cache={}
        # for i in range(len(obstacleGrid)):
        #     for j in range(len(obstacleGrid[0])):
        #         if obstacleGrid[i][j]==1:
        #             cache[(i,j)]=0
        

        # if (0,0) in cache:
        #     return 0
        # cache[(0,0)]=1

        # def get_unique_path(m,n):
        #     if (m,n) in cache:
        #         return cache[(m,n)]
        #     if m==0:
        #         val = get_unique_path(m,n-1)
        #         cache[(m,n)]=val
        #         return cache[(m,n)]
        #     if n==0:
        #         val = get_unique_path(m-1,n)
        #         cache[(m,n)]=val
        #         return cache[(m,n)]
        #     cache[(m,n)]=get_unique_path(m,n-1) +get_unique_path(m-1,n)  
        #     return cache[(m,n)]
          

        # return get_unique_path(m,n)

        ##############################################

        # recursive solution

        ############################################


        # recursive solution
        # m = len(obstacleGrid)-1
        # n = len(obstacleGrid[0])-1

        # def recursive_solution(m,n):
        #     if m==0 and n==0:
        #         return 1 if obstacleGrid[m][n]==0 else 0

        #     if obstacleGrid[m][n]==1:
        #         return 0
            
        #     if m==0:
        #         return recursive_solution(m,n-1)
            
        #     if n==0:
        #         return recursive_solution(m-1,n)

        #     return recursive_solution(m,n-1)+recursive_solution(m-1,n)
        # return recursive_solution(m,n)