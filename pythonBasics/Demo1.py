# list is data type
values = [2, 4, "ragahv", 6, 7, 8, 50]
print(values[0])
print(values[2])

print(values[1:3]) # print between data
print(values[-1]) # print last
values.index(4)
values.insert(3, "Naidu")

print(values)

values.append("sai")
values.append("sudhan")
print(values)

values[0] = "Testing" # add new
values[2] = "Testing" # add new

del values[5] # to delete
print(values)

# Tuple data type:
# (List is Mutable ( means updatable) but Tuple is Unmutable (can not update), and this is the only difference btw them)

val = (1, 2, 4, "Test")

print(val[3])
print(val)
#vel[3] = "Raghav" # update is not possible with Tuples
print(val[0])

# Dictionary data type

dic = {"test": 1, 3: "raghav", "c": "Testing"}
print(dic[3])
print(dic["c"])

#Loading data into dictionaries
dict = {}
dict["FirstName"] = "Raghav"
dict["LstName"] = "Naidu"
dict["Gender"] = "Male"
print(dict)
print(dict["Gender"])
