import numpy as np

def CheckMatrix(a):
    kt=0
    count_cheo1 = 0
    count_cheo2 = 0
    if(len(a[0])!= len(a[:][0])):
        return False
    for i in range(0,len(a[0])):
        kt += a[0][i]
    print(kt)
    count_ngang = kt
    for i in range(0,len(a[0])):
        if(count_ngang!=kt):
            return False
        count_ngang=0
        for j in range(0,len(a[:][0])):
            count_ngang += a[i][j]

    count_doc = kt
    for i in range(0,len(a[0])):
        if(count_doc!=kt):
            return False
        count_doc=0
        for j in range(0,len(a[:][0])):
            count_doc += a[j][i]

    for i in range(0,len(a[0])):
        for j in range(0,len(a[:][0])):
            if(i==j):
                count_cheo1 += a[i][j]
    if(count_cheo1!=kt):
        return False

    for i in range(0, len(a[0])):
        for j in range(0, len(a[:][0])):
            if (j == len(a[0])-i-1):
                count_cheo2 += a[i][j]
    if(count_cheo2!=kt):
        return False

    # print(count_ngang)
    # print(count_doc)
    # print(count_cheo1)
    # print(count_cheo2)

    if(count_ngang==count_doc):
        return True

    return False

if __name__ == '__main__':
    a = np.array([[1, 1, 1], [1, 1, 1],[1, 1, 1]])
    # print(a)
    b = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    # print(b)
    c = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    # print(c)

    # CheckMatrix(a)

    # print(CheckMatrix(a))
    if(CheckMatrix(b)):
        print("La ma tran Matrix Square")
    else:
        print("Khong la ma tran Matrix Square")