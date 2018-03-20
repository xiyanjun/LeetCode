import math
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        p1p2=math.sqrt((p1[1]-p2[1])**2+(p1[0]-p2[0])**2)
        p1p3=math.sqrt((p1[1]-p3[1])**2+(p1[0]-p3[0])**2)
        p1p4=math.sqrt((p1[1]-p4[1])**2+(p1[0]-p4[0])**2)
        p2p3=math.sqrt((p2[1]-p3[1])**2+(p2[0]-p3[0])**2)
        p2p4=math.sqrt((p2[1]-p4[1])**2+(p2[0]-p4[0])**2)
        p3p4=math.sqrt((p3[1]-p4[1])**2+(p3[0]-p4[0])**2)
        if p1p2==p1p3==p2p4==p3p4 and p1p2!=0:
            if p1p4==p2p3 and p1p4!=0:
                return True
        if p1p2==p1p4==p2p3==p3p4 and p1p2!=0:
            if p1p3==p2p4 and p1p3!=0:
                return True
        if p1p3==p1p4==p2p4==p2p3 and p1p3!=0:
            if p1p2==p3p4 and p1p2!=0:
                return True
        return False
def main():
    p1=[0,0]
    p2=[1,1]
    p3=[1,0]
    p4=[0,1]
    solution=Solution()
    result=solution.validSquare(p1,p2,p3,p4)
    print(result)
if __name__=='__main__':
    main()