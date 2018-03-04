class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        Parentheses={'(':0,')':1,'[':3,']':4,'{':6,'}':7}
        s=list(s)
        Paren=[]
        for i in range(len(s)):
            if i==0 or len(Paren)==0:
                Paren.append(s[i])
            else:
                if Parentheses[s[i]]==Parentheses[Paren[-1]]+1:
                    Paren.pop()
                else:
                    Paren.append(s[i])
        if Paren==[]:
            return True
        else:
            return False
if __name__=='__main__':
    solution=Solution()
    outbool=solution.isValid('[')
    print(outbool)

