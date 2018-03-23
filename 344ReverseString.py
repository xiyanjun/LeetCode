class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        size=len(s)
        s=list(s)
        for i in range(int(size//2)):
            s[i],s[size-1-i]=s[size-1-i],s[i]
        res=''
        for i in s:
            res+=i
        return res
def main():
    s='hello'
    solution=Solution()
    result=solution.reverseString(s)
    print(result)
if __name__=='__main__':
    main()