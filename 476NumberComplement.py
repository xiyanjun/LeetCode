class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i=1
        while i<=num:
            num^=i
            i=i<<1
        return num
def main():
    num=5
    solution=Solution()
    result=solution.findComplement(num)
    print(result)
if __name__=='__main__':
    main()