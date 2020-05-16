
# IF else loops
greeting = "Good Morning"
if greeting == "Morning":
    print("condition matched")
else:
    print("condition not matched")

print("if loops completed")

a = 5
if a > 4:
    print("condition matched")
else:
    print("condition not matched")

print("if loops completed")


# For loops

obj =[2, 4, 5, 6, 7, 8]
for i in obj:
    print(i*2)

# sum of first numbers
summary = 0
for j in range(1,6):
    summary = summary+j
print("Sum of all 1 to 5 numbers: ", summary)

print ("******************")

for k in range(1, 10, 2): # jump 2 number
   print(k)

print ("******************")

for m in range(10): # all number with zero index
   print(m)

#While loop

print ("******************")

it = 5
while it > 2:
    print(it)
    it = it-1
print("while loop done")


print ("******************")

itt = 10
while itt > 1:
    if itt == 9:
        itt = itt - 1
        continue
    if itt != 3:
        break
    print(itt)
print("while loop done last test")
