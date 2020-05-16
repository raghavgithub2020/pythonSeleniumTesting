file = open('test.txt')
print(file.read(3)) # read the content file

# read line by line
print(file.readline())
print(file.readline())

#read all line one by one

line = file.readline()
while line != "":
    print(line)
    line = file.readline()

for line in file.readlines(): # read as like list
    print(line)
# with open('test.txt') as file:
# file.close()


# Read the file and store all the lines in list
# reverse the list
# write the list back to the file
with open('test.txt', 'r') as reader:
    content = reader.readlines() # read all line
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)





