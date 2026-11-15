class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=list(s)
        ans=''
        for i in a:
            if i>='A' and i<='Z':
                ans+=chr(ord(i)+32)
            elif i>='a' and i<='z':
                ans+=i
            elif i>='0' and i<='9':
                ans+=i
            elif i==' ':
                pass
            else:
                pass
        return ans==ans[::-1]