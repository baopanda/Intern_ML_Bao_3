import numpy as np
import random

if __name__ == '__main__':
    # a = np.arange(10000).reshape(100,100)
    a = np.eye(100)
    print(a)
    for i in range(0, 100):
        for j in range(0, 100):
            a[i][j] = random.randint(0, 100)

    print(a)
    print(a.shape)

    b = np.transpose(a)
    print(b)
    print(np.linalg.det(a))

    w, v = np.linalg.eig(a)

    print(w)
    print(v)

    with open("output.txt","w",encoding='utf-8') as file:
        file.write("Ma tran a la: ")
        for i in range(0, 100):
            for j in range(0, 100):
               file.write("%-4d" % a[i][j])
            file.write("\n")

        file.write("Ma tran chuyen vi cua a la: ")
        for i in range(0, 100):
            file.write("\n")
            for j in range(0, 100):
               file.write("%-4d" % b[i][j])

        file.write("\nDinh Thuc cua a la: " + str(np.linalg.det(a)))
        file.write("\nGia tri rieng cua a la: \n" + str(w))
        file.write("\n Vector rieng cua a la: \n" + str(v))