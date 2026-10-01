for i in range(3):
    for j in range(3):
        print(f"({i} , {j})")

# f shape 
numbers = [5,2,5,2,2]
for i in numbers:
    # print('*'*i)   
    for j in range(i):
        print('*' , end='')   
    print()      