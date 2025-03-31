class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check x is negative
        if x<0:
            return False
        # convert to string
        str_num = str(x)
        
        # iterate digit from number
        for index in range(len(str_num)//2):
            # checking 
            if str_num[index]!= str_num[-index-1]:
                return False
        return True 
        