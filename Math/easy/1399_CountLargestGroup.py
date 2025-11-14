def SumOfDigits(n):
    return sum(map(int,str(n)))

class Solution:
    def countLargestGroup(self, n: int) -> int:
        memo=dict()
        for i in range(1,n+1):
            key=SumOfDigits(i)
            memo[key]=memo.get(key,0)+1
        freq=list(memo.values())
        mode = max(freq)
        return freq.count(mode)
        