class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # ###########################
        # recusive solution

        # ###########################

        # def recursive_solution(numRows:int):
        #     if numRows==1:
        #         return [[1]]
        #     if numRows==2:
        #         return [[1],[1,1]]
        #     out_list = recursive_solution(numRows-1)
        #     temp=[1]
        #     last_row=out_list[-1]
        #     for i in range(0,len(last_row)-1):
        #         temp.append(last_row[i]+last_row[i+1])

        #     temp.append(1)
        #     out_list.append(temp)
        #     return out_list

            
        
        # return recursive_solution(numRows)
        
        # ###########################
        # memorisation
        # ###########################

        # memo={}
        # memo[1]=[[1]]
        # memo[2]=[[1],[1,1]]

        # def memorisation(numRows):
        #     if numRows in memo:
        #         return memo[numRows]
        #     val = memorisation(numRows-1)
            
        #     last_row = val[-1]
        #     output =[1]
        #     for i in range(1,len(last_row)):
                
        #         output.append(last_row[i]+last_row[i-1])
        #     output.append(1)
        #     val.append(output)
        #     memo[numRows]=val
        #     return memo[numRows]
        # return memorisation(numRows)

    
        # ###########################
        # tabularisation
        # ###########################

        def tabularisation(numRows):
            
            if numRows==1:
                return [[1]]
            if numRows==2:
                return [[1],[1,1]]
            
            memo=[[1],[1,1]]
            for i in range(3,numRows+1):
                output =[1]
                temp_list = memo[-1]
                for j in range(1,len(temp_list)):
                    output.append(temp_list[j]+temp_list[j-1])
                output.append(1)
                memo.append(output)
            return memo
        return tabularisation(numRows)