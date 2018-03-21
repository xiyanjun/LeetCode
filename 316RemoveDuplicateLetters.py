class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        visit=[False]*26
        cnt=[0]*26
        for i in s:
            cnt[ord(i)-97]+=1
        ans=[]
        for i in s:
            cnt[ord(i)-97]-=1
            if visit[ord(i)-97]:
                continue
            while ans and ans[-1]>i and cnt[ord(ans[-1])-97]:
                visit[ord(ans.pop())-97]=False
            ans.append(i)
            visit[ord(i)-97]=True
        return ''.join(ans)
def main():
    s='bcabc'
    solution=Solution()
    result=solution.removeDuplicateLetters(s)
    print(result)
if __name__=="__main__":
    main()


