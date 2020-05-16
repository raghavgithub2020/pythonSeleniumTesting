str = "Raghav Testing"
str1 = " Naidu Testing"
str2 = "Naidu"

print(str[1])
print(str[0:5])
print(str + str1)

print(str2 in str) # sub string check

var = str.split(" ")
print(var)
print(str[0])

str4 = " Raghav  "
print(str4.strip()) # to remove any spaces
print(str4.lstrip()) # to remove left spaces
print(str4.rstrip()) # to remove right spaces