class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(s)-1,-1,-1):
            j=0
            while i+j<=len(s)-1:
                if s[j:i+j+1]==s[j:i+j+1][::-1]:
                    return s[j:i+j+1]
                else:
                    j+=1
def main():
    s='babab'
    solution=Solution()
    result=solution.longestPalindrome(s)
    print(result)
if __name__=='__main__':
    main()

