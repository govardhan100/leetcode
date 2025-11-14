def diff(p1,p2):
    x1,y1 =p1
    x2,y2= p2
    if x1==x2:
        return '90'
    return (y2-y1)/(x2-x1)



class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        slopes=set()
        p1 = coordinates[0]
        for index in range(1,len(coordinates)):

           
            p2 = coordinates[index]
            value = diff(p1,p2)
            slopes.add(value)
            #print(slopes)
            if index>1 and len(slopes)>1:
                return False
        return True

