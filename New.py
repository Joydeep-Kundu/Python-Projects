class Solution(object):
    def longestValidParentheses(self, s):
        l=[]
        i=0
        c=0
        ci=0
        while(i<len(s)):
            if s[i]=='(':
                l.append('(')
            elif(s[i]==')'):
                l.append(')')
            if(i>0):
                if s[i]==')' and l[len(l)-2]=='(':
                    c+=2
                    l.pop()
                    l.pop()
                    if(i-2!=ci and c>=2):
                        c=0
                    ci=i
            print(l)
            i+=1
        return c
o=Solution()
print(o.longestValidParentheses("()(()"))