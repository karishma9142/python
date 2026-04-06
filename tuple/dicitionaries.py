customer = {
    "name" : 'karishma',
    "age" : 19 ,
    'is_verified' : True
}

print(customer["name"])
print(customer.get("name"))
print(customer.get("birthday" , 'july 7 , 2006'))
# print(customer['birthday']) gives error