tup = (1, 10, 4, True, "str")
print(tup[1])  # this outputs 10
print(tup[-1])  # this outputs "str"
tup[1] = 0  # this raises an exception
tup.append(1)  # this raises an exception