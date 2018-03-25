class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        L=s.split()
        L.reverse()
        res=' '.join(L)
        return res
def main():
    s='the sky is blue'
    solution=Solution()
    result=solution.reverseWords(s)
    print(result)
if __name__=='__main__':
    main()