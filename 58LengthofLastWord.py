class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or len(s.replace(' ',''))==0:
            return 0
        lenth=len(s.strip().split()[-1])
        return lenth
if __name__=='__main__':
    s='Hello World'
    solution=Solution()
    result=solution.lengthOfLastWord(s)
    print(result)