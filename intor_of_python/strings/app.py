# text1='hello how are you' #for single line

# text2="i'm fine" #for single line

# text3='''oh nice
# what are you ding on weekend
# lets go on a trip''' #for multiple line

# print(text1)
# print(text2)
# print(text3)

course='ncdhcwiuedhwi ncuwehu'
course2=course[:] # copy of course

print(course[2]) # print d from begin (start from 0)
print(course[-2]) # print h from last (start from 1)

print(course[0:]) # print all
print(course[:5]) # print 0 to 5 (s exclude)
print(course[1:-1]) #print 1 to -1(last one => n)

# f formating string

first = 'karishma'
last = 'Rawat'
message = first + '[' +last+ '] is a coder '
msg = f'{first} [{last}] is a coder' # f formating

print(message)
print(msg)

