w = True  # <- Change this
x = True  # <- Change this
y = False  # <- Change this
z = True  # <- Change this

# Don't change any of these `condition_` variables.
condition_1 = w and x and not y or not z
condition_2 = not (w and not w) # demorgans law -> not w or w
condition_3 = not (w and y or y) # demorgans law -> not w or not y and not y
condition_4 = x and (y or z and w)

# All of these should print `True`.
print(condition_1)
print(condition_2)
print(condition_3)
print(condition_4)