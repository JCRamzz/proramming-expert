def sort_employees(employees, sort_by):

    if sort_by == 'name':
        sort_by = 0
    elif sort_by == 'age':
        sort_by = 1
    else:
        sort_by = 2

    def Key(e):
        return e[sort_by]

    newLst = sorted(employees, key=Key)
    return newLst