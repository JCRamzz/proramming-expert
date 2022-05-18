'''
lst = ["tim", "is", "the", "best", "instructor"]
string = "..."
tupl = ("and", "he", "is", "great")

for word in lst:
    print(word)
for i in string:
    print(i)
for each in tupl:
    print(each)
'''

'''
string1 = "aabbcsdw"
string2 = "abbbcsdd"

for index, element in enumerate(string1):
    if element == string2[index]:
        print(element)
'''
'''
lst = [45, 24, 22, 1, 45, 2, 12, 13, 16, 10, 0, -7]

for i in range(1, len(lst), 2):
    if lst[i] % 2 == 0:
        print(lst[i])
'''
'''
lst = [[2, 3, 4], [-2, -4, 0], [1, 2], [1, 1, 1, 5, 6], [0, 9, 8, 7]]

sum = 0

for i in lst:
    sum = 0
    for j in i:
       sum += j
    print(sum)
'''
lst = [-2, 0, 4, 5, 1, 2]

for i in range(len(lst)):
    if i + 1 == len(lst):
        break
    print(lst[i] + lst[i + 1])


