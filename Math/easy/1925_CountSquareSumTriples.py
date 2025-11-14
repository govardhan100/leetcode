class Solution:
    def countTriples(self, n: int) -> int:
        square_num=[i*i for i in range(1,n+1)]
        square_set =set(square_num)
        count =0
        for i in square_num:
            for j in square_num:
                if i+j in square_set:
                    count+=1
        return count
        