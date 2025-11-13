class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        memo={}
        memo['2']='abc'
        memo['3']='def'
        memo['4']='ghi'
        memo['5']='jkl'
        memo['6']='mno'
        memo['7']='pqrs'
        memo['8']='tuv'
        memo['9']='wxyz'

        for key in memo:
            memo[key]=list(memo[key])

        # output=[]

        # for digit in digits:
        #     char_list = memo.get(digit)
        #     if len(output)==0:
        #         output= char_list
        #         continue
        #     temp=[]
        #     for item in output:
        #         for char in char_list:
        #             temp.append(item+char)
        #     output = temp
        # return output
        def recursive_solution(digits,output):
            if len(digits)==0:
                return output
            temp =[]
            
            for char in memo.get(digits[-1]):
                if not output:
                    temp.append(char)

                for item in output:
                    temp.append(char+item)
            output =temp
            
            return recursive_solution(digits[0:-1],output)
        output =[]
        return recursive_solution(digits,output)
            




        