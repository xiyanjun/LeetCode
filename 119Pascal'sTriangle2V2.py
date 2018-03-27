class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        from scipy.special import comb
        res=[]
        for i in range(rowIndex+1):
            res.append(int(round(comb(rowIndex,i))))
        return res
def main():
    rowIndex=31
    solution=Solution()
    result=solution.getRow(rowIndex)
    print(result)
if __name__=='__main__':
    main()