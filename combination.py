def combi(n, m):
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi(n-1, m) + combi(n-1, m-1)

n = int(input("n: "))
m = int(input("m: "))
print(combi(n, m))