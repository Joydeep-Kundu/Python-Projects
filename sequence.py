from posixpath import split


# str=input('enter a string:- ');
# print(str);
# print(str[:3],str[2:]);
#str[2]=d;

#list

# l=input('enter list using "," separator: ');
# l=l.split(',');
# print(l);
# l=[int(i) for i in l];
# print(l);
# print(l[:2]);
# l.append(3);
# print(l);
# l.pop(2);
# print(l);


#dictionary

# di={};
# di['100']='red';
# di['000']='white';
# di['010']='green';
# di['001']='blue';
# di['111']='black';
# print(di);

#Set 

# set1={};
# set2={};
# l=input('enter set1 using "," separator: ');
# l=l.split(',');
# l=[int(i) for i in l];
# set1=set(l);
# l=input('enter set2 using "," separator: ');
# l=l.split(',');
# l=[int(i) for i in l];
# set2=set(l);
# print(set1);
# print(set2);
# print('set difference ',set1-set2);
# print('set difference ',set2-set1)
# print('uninon ',set1|set2)
# print('intersection ',set1&set2)
# print('symantric ',set1^set2);
# set1.pop();
# print(set1);
# set1.add(4);
# print(set1);
# set1.remove(4);
# print(set1);
# set1.clear();
# print(set1);


#tuple


l=input('enter set1 using "," separator: ');
l=l.split(',');
tu=tuple(l);
print(tu);