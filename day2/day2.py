def is_valid_report(r, recur) -> bool:
    valid = True
    asc = r[0] < r[1]
    for i in range(len(r)-1):
        if r[i] == r[i+1]: # adjacent value can't be equal
            valid = False
            # print(r, ' is not valid')
        # adjacent values can't break the ascending or descending pattern
        elif (r[i] > r[i+1] and asc) or (r[i] < r[i+1] and not asc):
            valid = False
            # print(r, ' is not valid')
        # adjacent values can't have a difference greater than 3
        elif abs(r[i] - r[i+1]) > 3:
            valid = False
            # print(r, 'is not valid (too great an difference)')
    if valid:
        # print(r, ' is valid')
        return True
    elif recur:
        for i in range(len(r)):
            # temp = r.copy()
            temp = r[:i] + r[i+1:]  # Create a new list by slicing
            if is_valid_report(temp, False):
                print(f'{r} becomes valid by removing {r[i]}')
                return True
    else:
        return False

with open('input2.txt') as f:
    reports = f.read().splitlines()
    reports = [[int(s) for s in r.split()] for r in reports]
    num_valid = 0
    for r in reports:
       if is_valid_report(r, True):
           num_valid += 1
    print(num_valid)