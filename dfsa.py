# s=[]
# for i in range(int(input())):
#     s.append(input()[1:])
#     ins=s[i].index(' ')
#     s[i]=s[i][:ins+1]+s[i][ins+2:]
#     s[i]=s[i][::-1]
# print(s)
age=[21,32,19,17,30,17,20,8]
for i in range(len(age)):
    if age[i]%2==0:
        age[i]='even'
print(age)