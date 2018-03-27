class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        ransomcount=collections.Counter(ransomNote)
        magazinecount=collections.Counter(magazine)
        return not ransomcount-magazinecount
def main():
    ransomNote='a'
    magazine='b'
    solution=Solution()
    result=solution.canConstruct(ransomNote,magazine)
    print(result)
if __name__=='__main__':
    main()