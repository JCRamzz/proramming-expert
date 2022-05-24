def pairs_sum_to_target(list1, list2, target):
    pairs = []
    for i, value in enumerate(list1):
        for j, value2 in enumerate(list2):
            if value + value2 == target:
                pairs.append([i, j])  # appending a new list

    return pairs

