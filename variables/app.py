n=10
name='karishma'
istrue = True
print(type(n))
print(type(name))
print(type(istrue))

# input in python

n=input('enter a number ')
print (n)

name=input('enter your name ')
color=input('enter your favourite color ')

# You must ensure everything is a string
print(name + ' likes ' + color)

# Converts non-strings to string automatically
print(name , ' likes ' , color)

# different ways of print in python

print('karishma')
input('karishma')
exit('karishma')
quit('karishma')
raise SystemExit('karishma')

import sys
sys.stdout.write('karishma')
a=print
a('karishma')


# Python takes input as a string (str) by default, 
# so if you want a specific data type, you need to convert it explicitly.

age=int(input('enter your age '))
print (age)