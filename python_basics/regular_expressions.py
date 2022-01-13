import re

text = "This green car is very fast"
pattern = "car"

found = re.search(pattern, text)
if(found):
    initial = found.start()
    final = found.end()
    print("Pattern found in the text from char number {} to char number {}".format(initial, final))

else:
    print("Pattern not found in the text")

# more than 1 match case

text1 = "purple is my favorite color, that is why my computer is purple"
pattern1 = "purple"
result = re.findall(pattern1, text1)
print(result)
times = len(result)
print(times)
# You can look for more than one pattern, in that case pattern1 can be a list of the patterns to find
# then you can use a bucle to look for each pattern in the list
