class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        memo={}
        if len(s)<=10:
            return []
        for i in range(10,len(s)+1):
            
            sub = s[i-10:i]
            memo[sub]=memo.get(sub,0)+1
        output =[key for key,value in memo.items() if value>1]
        return output
        

        