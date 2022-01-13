def function1():
    print("Hello, human!")

function1()

def sum(number1, number2):
    if type(number1) == type(number2) == type(10):
        result = number1 + number2
    else:
        result = "Ups. The variables are not numbers"
    return result

print(sum(1, 6))
print(sum("Uno", "Dos"))

# use """ in functions to explain what they do 
