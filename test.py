class Solution:
    def intToRoman(self, num: int) -> str:
        d={1:'I',5:'V',10:"X",50:"L",100:"C",1000:'M'}
        di={4:"IV",9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        i=0
        s=''
        while(num>0):
            if(num%10 in di):
                print(num)
                s=di[i]+s
            elif(num%10 in d):
                print(num)
                s=d[i]+s
            num=num//10
            print(s)
        return s

p=Solution()
print(p.intToRoman(111))