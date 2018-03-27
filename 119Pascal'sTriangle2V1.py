class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nowrow=[1]
        nowIndex=rowIndex+1
        if nowIndex==1:
            return nowrow
        if nowIndex>1:
            for i in range(2,nowIndex+1):
                prerow=nowrow
                nowrow=[1]
                for j in range(i-2):
                    nowrow.append(prerow[j]+prerow[j+1])
                nowrow.append(1)
            return nowrow
def main():
    rowIndex=0
    solution=Solution()
    result=solution.getRow(rowIndex)
    print(result)
if __name__=='__main__':
    main()