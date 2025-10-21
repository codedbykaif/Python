def my_decorator(func):
    def wrapper():
        print("something is happening before the function is called")
        func()
        print("Somehting is happening after the function is called")
    return wrapper   


@my_decorator
def say_hello():
    print("hello")

say_hello()    

