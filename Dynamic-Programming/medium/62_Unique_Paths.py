def nCr(n,r):
    """ calculate nCr """
    # base cases
    if r>n:
        return 0
    if n==r or r==0:
        return 1
    # optimization
    r=min(n-r,r)
    result =1
    # calculate nCr
    for i in range(1,r+1):
        result=(result*((n-r+i)))/i
        
    return int(result)



    


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # ##############################

        # -----recursively -----
        
        # ##############################
        # if m==1 and n==1:
        #     return 1
        # if m==1:
        #     return self.uniquePaths(m,n-1)
        # if n==1:
        #     return self.uniquePaths(m-1,n)

        # return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        
        # ##############################

        # Memorisation
        
        ################################
        
        # memo={(1,1):1}
        # def paths(m,n):
        #     if (m,n) in memo:
        #         return memo[(m,n)]
        #     if m==1:
        #         memo[(m,n)]=paths(m,n-1)
        #         return memo[(m,n)]
        #     if n==1:
        #         memo[(m,n)]=paths(m-1,n)
        #         return memo[(m,n)]
        #     value = paths(m,n-1)+paths(m-1,n)
        #     memo[(m,n)]=value
        #     return memo[(m,n)]
        # return paths(m,n)
        ##############################################
        
        # -------Tabularistion------

        #############################################

        # table=[[0]*n for i in range(m)]
        # table[0][0]=1
        # for i in range(m):
        #     for j in range(n):
                
        #         if i==0 and j==0:
        #             table[0][0]=1
        #             continue
        #         val=0
        #         if i==0:
        #             table[i][j]=table[i][j-1]
        #             continue
        #         if j==0:
        #             table[i][j]=table[i-1][j]
        #             continue
        #         table[i][j]=table[i-1][j]+table[i][j-1]



        # return table[m-1][n-1]


        # combination (m+n-2)!/((m-1)!*(n-1)!)
        return nCr(m+n-2,m-1)
