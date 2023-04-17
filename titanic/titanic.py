import csv
import numpy as np

def surviveEncoder(survive):
    if survive == 0:
        return -1
    if survive == 1:
        return 1

def sexEncoder(sex):
    if sex == 'male':
        return 1
    if sex == 'female':
        return -1

def embarkedEncoder(embarked):
    if embarked == 'C':
        return 1
    if embarked == 'S':
        return 10
    if embarked == 'Q':
        return -10
    else:
        return 0

def cabinEncoder(cabin):
    if cabin == '':
        return -1
    else:
        return 1

def makeMatrix(array, matrix_x, matrix_y, i):
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    b = 0
    c = 0
    for info in array:
        if i == 0:
            a1 += info[1]
            a2 += info[2]
            a3 += info[3]
            a4 += info[4]
            a5 += info[5]
            a6 += info[6]
            a7 += info[7]
            a8 += info[8]
            b += 1
            c += info[0]
        else:
            a1 += info[1]*info[i]
            a2 += info[2]*info[i]
            a3 += info[3]*info[i]
            a4 += info[4]*info[i]
            a5 += info[5]*info[i]
            a6 += info[6]*info[i]
            a7 += info[7]*info[i]
            a8 += info[8]*info[i]
            b += info[i]
            c += info[0]*info[i]
    row = [a1, a2, a3, a4, a5, a6, a7, a8, b]
    matrix_x.append(row)
    matrix_y.append([c])
    return matrix_x, matrix_y

f = open('train.csv', 'r')
wb_train = csv.reader(f)

array = []
for i, line in enumerate(wb_train):
    info = []
    if i != 0:
        print(i)
        info = [surviveEncoder(int(line[1])), float(line[2]), sexEncoder(line[4]), float(line[5]), float(line[6]), float(line[7]), float(line[9]), cabinEncoder(line[10]), embarkedEncoder(line[11])]
        array.append(info)
print(*array, sep='\n')

matrix_x = []
matrix_y = []
for i in range(9):
    print(i)
    matrix_x, matrix_y = makeMatrix(array, matrix_x, matrix_y, i)
# print(*matrix_x, sep='\n')
# print(*matrix_y, sep='\n')

array_x = np.array(matrix_x)
array_y = np.array(matrix_y)
array_x_inv = np.linalg.inv(array_x)

answer = np.dot(array_x_inv, array_y)
print(answer)

# f = open('test.csv', 'r')
# wb_test = csv.reader(f)
# array_test = []
# for i, line in enumerate(wb_test):
#     info = []
#     if i != 0:
#         print(i)
#         info = [sexEncoder(line[3]), float(line[4]), float(line[8])]
#         array_test.append(info)
# print(*array_test, sep='\n')