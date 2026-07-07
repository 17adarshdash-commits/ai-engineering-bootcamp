def average(*args):
    total = 0
    for arg in args:
        total += arg
    return total / len(args)

print(average(10,20,30))