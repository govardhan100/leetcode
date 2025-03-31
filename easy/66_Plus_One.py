class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # initialisation of variable
        carry = 1
        rem =0
        total_nums = []
        # iterating nums
        for i in digits[::-1]:
            # carry out calculation
            rem = (i+carry)%10
            carry = (i+carry)//10
            total_nums.append(rem)
        # by end if we carry then add
        if carry ==1:
            total_nums.append(carry)
            return total_nums[::-1]
        # reverse the list
        return total_nums[::-1]