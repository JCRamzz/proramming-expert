w = 1  # <- Change this
x = 1  # <- Change this
y = 4  # <- Change this
z = -2  # <- Change this

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_slice = lst[::z]
second_slice = first_slice[:y]
third_slice = second_slice[x:]
last_slice = third_slice[::w]

print(last_slice)