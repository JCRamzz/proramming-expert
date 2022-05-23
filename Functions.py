def running_sums(numbers):

    for i in range(1, len(numbers)):
        sum = numbers[i] + numbers[i - 1]
        numbers.pop(i)
        numbers.insert(i, sum)

    return numbers


print(running_sums([]))
