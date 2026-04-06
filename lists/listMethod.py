numbers = [5 ,2 , 2,1,7,4]
numbers.append(4)
numbers.insert(1,10)
numbers.remove(1)
# numbers.clear()
numbers.pop()
print(numbers.index(10))
print(2 in numbers)
print(numbers.count(2))
numbers.sort()
print(numbers)

numbers2 = numbers.copy()
numbers.append(10)
print(numbers2)
print(numbers)

#  remove duplicates

num = [2 , 2 ,4 , 6, 3 , 4, 6 ,1]
for i in num :
    a = i
    if(num.count(a) >1) :
        num.remove(a)

print(num)        