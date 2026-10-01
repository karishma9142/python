# A method is a function that belongs to an object or class,
#  while a function is a general-purpose block of code that is not tied to any object.
# print() , len() => functions
# upper() => method

course='python course'
print(len(course))
print(course.upper()) # it does not modify the original one it make a duplicate copy
print(course)
print(course.find('o'))
print(course.find('course'))
print('course' in course)
print(course.replace('course' , 'courses')) # it does not modify the original one it make a duplicate copy
print(course)


