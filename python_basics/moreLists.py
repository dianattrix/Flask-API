list = [1,2,5,"Diana"]
print(list)

list.pop()
print(list)

list.pop(0)
print(list)

#there are more functions like reverse, sort, etc

list1 = [1,2,3,4,[8,7,6,5]]
print(list1)
print(list1[4][0])

#list comprehension: building a list from another one
matrix = [[1,2,3,4],[4,5,6],[7,8,9]]
newList = [matrix[0] for element in matrix]
print(newList)
