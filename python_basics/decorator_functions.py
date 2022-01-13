def something(function):
    def decorate():
        print("*******************************")
        function()
        print("*******************************")
    return decorate

@something
def printer():
    print("Hi!")

if __name__ != '__main__':
    print("This code is not from main.py")

#printer()
#printer = something(printer)
printer()
