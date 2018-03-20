class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)==len(B)==0:
            return True
        for i in range(len(A)):
            A=A[1:]+A[:1]
            if A==B:
                return True
        return False
def main():
    A='abcde'
    B='cdeab'
    solution=Solution()
    result=solution.rotateString(A,B)
    print(result)
if __name__=='__main__':
    main()