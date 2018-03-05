class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:len(needle)+i]==needle:
                return i
        return -1
if __name__=='__main__':
    solution=Solution()
    haystack='hello'
    needle='ll'
    result=solution.strStr(haystack,needle)
    print(result)