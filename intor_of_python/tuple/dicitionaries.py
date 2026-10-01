
'''
store key value pairs 
key should be unique other vise it will be going to override by new one
'''

customer = {
    "name" : 'karishma',
    "age" : 19 ,
    'is_verified' : True
}

# append new element
customer['price'] = 100

# update exiting element
customer['price'] = 90
print(customer)
print(customer["name"])
print(customer.get("name"))
print(customer.get("birthday" , 'july 7 , 2006'))
# print(customer['birthday'])
# print(customer['birthday']) gives error

# METHODS
print(customer.get("name"))

keys = customer.keys()
print(list(keys))

values = customer.values()
print(list(values))

all=customer.items()
print(list(all))

poped = customer.pop('name' , 'not found');
print(poped)

poped_i = customer.popitem();
print(poped_i)

customer.clear();
print(customer)

