# names = ['karishma' , 'banty','anvi','rekha']
# print(names[0])
# print(names[-0])
# print(names[2:])
# print(names[2:3])
# print(names[:])
# names[3]='Rekha'
# print(names)

# creation of s list 
list1=list(range(1,11,1))
print(list1)

# list comprehnsion
squres1=[];
for i in range (1,11):
   if(i%2==0):
        squres1.append(i**2)

print(squres1)

# same using list comprehnsion
squres2 = [i**2 for i in range(1,11) if (i%2==0)];
print(squres2)