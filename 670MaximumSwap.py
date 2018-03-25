class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        res=list(str(num))
        back=[res[len(res)-1]]
        for i in range(len(res)-2,-1,-1):
            if res[i]>=back[len(res)-2-i]:
                back.append(res[i])
            else:
                back.append(back[len(res)-2-i])
        back.reverse()
        for i in range(len(res)-1):
            if back[i]==res[i]:
                continue
            else:
                for j in range(i+1,len(res)):
                    if back[j]!=back[i]:
                        res[i],res[j-1]=res[j-1],res[i]
                        break
                    elif j==len(res)-1:
                        res[i],res[j]=res[j],res[i]
                        break
            break
        return int(''.join(res))
def main():
    num=2736
    solution=Solution()
    result=solution.maximumSwap(num)
    print(result)
if __name__=='__main__':
    main()