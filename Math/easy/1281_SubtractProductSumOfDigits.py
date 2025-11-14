class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        number=map(int,str(n))
        product,summation =1,0
        for i in number:
            product*=i
            summation+=i
        return product - summation