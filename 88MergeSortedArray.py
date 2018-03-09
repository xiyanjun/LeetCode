class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]=nums2[:n]
        nums1.sort()
def main():
    nums1=[1]
    m=1
    nums2=[]
    n=0
    solution=Solution()
    solution.merge(nums1,m,nums2,n)
    print(nums1)
if __name__=='__main__':
    main()
