list = [1,2,3,4,5,6,7,8,9,10]
print(list)

list1 = [11,1,2,14,"Pingu",5,"Diana"]
print(list1)

element = list1[3]
print(element)

newElements = ['red','green','blue']
list1.append(newElements)
print(list1) #adds the list, not element by newElements
#if you want separated elements you need to use extend instead of append

newElements1 = ['red','green','blue']
list1.extend(newElements)
print(list1)
