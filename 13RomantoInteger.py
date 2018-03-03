class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
#罗马数字共有7个，即I（1）、V（5）、X（10）、L（50）、C（100）、D（500）和M（1000）
        numerals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum=0
        s=s[::-1]
        last=None
        for i in s:
            if last and numerals[i]<last:
                sum=sum-2*numerals[i]
            sum=sum+numerals[i]
            last=numerals[i]
        return sum
if __name__=='__main__':
    solution=Solution()
    outint=solution.romanToInt('DCXXI')
    print(outint)


