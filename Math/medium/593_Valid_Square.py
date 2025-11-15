def distance(p1,p2):
    x1,y1 =p1
    x2,y2 =p2
    return pow(pow(y2-y1,2)+pow(x2-x1,2),0.5)

def angle(p1,p2,p3):
    x1,y1=p1
    x2,y2=p2
    x3,y3=p3
    
    v1x =x2-x1
    v2x =x3-x1
    v1y =y2-y1
    v2y =y3-y1
    return (v1x*v2x)+(v2y*v1y)
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        distance_set=set()
        angle_set =set()
        a = distance(p1,p2)
        b = distance(p2,p3)
        c = distance(p3,p4)
        d = distance(p4,p1)
        e = distance(p4,p2)
        f = distance(p1,p3)

        distance_set.add(a)
        distance_set.add(b)
        distance_set.add(c)
        distance_set.add(d)
        distance_set.add(e)
        distance_set.add(f)
        
        a_angle=angle(p1,p2,p4)
        b_angle =angle(p2,p1,p3)
        c_angle = angle(p3,p2,p4)
        d_angle = angle(p4,p3,p1)
        angle_set.add(a_angle)
        angle_set.add(b_angle)
        angle_set.add(c_angle)
        angle_set.add(d_angle)
        #print(angle_set,distance_set)
        a=min(distance_set)
        b =max(distance_set)
        if abs((2*(a**2))-(b**2))>1e-5:
            return False
        if len(angle_set)==1 and len(distance_set)==2:
            return True
        return False
        


        