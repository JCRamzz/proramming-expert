w = "hell"  # <- Change this
x = "hello"  # <- Change this
y = x  # <- Change this
z = "d"  # <- Change this

# Don't change any of these `condition_` variables.
condition_1 = w != "a"
condition_2 = w < x
condition_3 = x == y
condition_4 = y == "hello"
condition_5 = z > "c"

# All of these should print `True`.
print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)
print(condition_5)