import time

n = int(input("number of elements: "))
haystack = [k for k in range(n)]

print("searching for the maximum value...")

ts = time.time()
maximum = max(haystack)
elapsed = time.time() - ts

print("maximum element = {}, elapsed time = {}".format(maximum, elapsed))