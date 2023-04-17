def binsearch(my_list, x, lower, upper):
    if x < my_list[lower] or x > my_list[upper]:
        return -1
    mid = (lower + upper) // 2
    if my_list[mid] == x:
        return mid
    elif x < my_list[mid]:
        return binsearch(my_list, x, lower, mid)
    else:
        return binsearch(my_list, x, mid, upper)

my_list = [0, 1, 2, 3, 4, 5, 6]
x = int(input("x: "))
print(binsearch(my_list, x, 0, len(my_list) - 1))