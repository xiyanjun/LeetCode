class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        newdigits=digits[:]
        newdigits[0]=(digits[0]+1)%10
        flag=(digits[0]+1)//10
        for i in range(1,len(newdigits)):
            newdigits[i]=(digits[i]+flag)%10
            flag=(digits[i]+flag)//10
        if flag==1:
            newdigits.append(1)
        newdigits.reverse()
        return newdigits
if __name__=='__main__':
    digits=[0]
    solution=Solution()
    result=solution.plusOne(digits)
    print(result)
