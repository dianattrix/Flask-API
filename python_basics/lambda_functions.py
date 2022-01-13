list1 = [1,2,3,4,5]

filter = filter(lambda number : (number % 2) == 0, list1)
print(list(filter))
