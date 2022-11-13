# # def searchkey(d,k):
# #     if k in d.keys():
# #         return True;

# # def romtoint():
# #     rn=input()
# #     dx={'XL':40,"XC":90,"CD":400,"CM":900,'IX':9,"IV":4}
# #     d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# #     i=0
# #     s=0
# #     while(i<len(rn)-1):
# #         if(searchkey(dx,rn[i]+rn[i+1])==True):
# #             s+=dx[rn[i]+rn[i+1]]
# #             i+=1;
# #         elif(searchkey(d,rn[i])==True):
# #             s+=d[rn[i]]
# #         i+=1;
# #     if(len(rn)-1==i and searchkey(d,rn[i])==True):
# #         s+=d[rn[i]]
# #     print(s)
# # romtoint()

# class Solution:
#     def searchkey(self,d,k):
#         if k in d.keys():
#             return True;
    
#     def romanToInt(self, s):
#         rn=s
#         dx={'XL':40,"XC":90,"CD":400,"CM":900,'IX':9,"IV":4}
#         d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#         i=0
#         s=0
#         while(i<len(rn)-1):
#             if(self.searchkey(dx,rn[i]+rn[i+1])==True):
#                 s+=dx[rn[i]+rn[i+1]]
#                 i+=1;
#             elif(searchkey(d,rn[i])==True):
#                 s+=d[rn[i]]
#             i+=1;
#         if(len(rn)-1==i and searchkey(d,rn[i])==True):
#             s+=d[rn[i]]
#         print(s)

class Solution:
    def twoSum(self, nums,target):
        i=0
        while(i<len(nums)-1):
            j=i+1
            while(j<len(nums)):
                print(i,j)
                if(nums[i]+nums[j]==target):
                    return [i,j]
                j+=1
            i+=1;
op=Solution()
print(op.twoSum([3,5,7,9,4],12))