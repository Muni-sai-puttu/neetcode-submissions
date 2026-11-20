class Solution:
    def isValid(self, s: str) -> bool:

        a=list(s)
        ans=[]
        for i in a:
            if (i==']' or i==')' or i=='}') and len(a)==0:
                return False
            elif (i=='[' or i=='{' or i=='('):
                ans.append(i)
            elif (i==']' and ans[-1]=='[') or (i=='}' and ans[-1]=='{') or (i==')' and ans[-1]=='(') :
                ans.pop()
            else:
                return False
        return len(ans)==0