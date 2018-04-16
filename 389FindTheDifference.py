class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ss=[0]*26
        tt=[0]*26
        for i in s:
            ss[ord(i)-ord('a')]+=1
        for i in t:
            tt[ord(i)-ord('a')]+=1
        for i in range(26):
            if ss[i]!=tt[i]:
                return chr(ord('a')+i)
def main():
    s='abcd'
    t='abcde'
    solution=Solution()
    result=solution.findTheDifference(s,t)
    print(result)
if __name__=='__main__':
    main()