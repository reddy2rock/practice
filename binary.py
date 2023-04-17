target = int()
my_list = []

lower = 0
upper = len(my_list) - 1

while lower <= upper:
    middle = (lower + upper) // 2
    if my_list[middle] == target:
        break
    elif my_list[middle] < target:
        lower = middle + 1
    else:
        upper = middle
print(middle)