def my_decorater(func):
    def wrapper():
        print('Something is happening before function is called')
        func()
        print('Something is happening after function is called')
    return wrapper

@my_decorater
def say_hello():
    print('hello')    

say_hello()    