import datetime
import pandas as pd
import matplotlib.pyplot as plt
from math import *

def ConvertTime(a):
    b = datetime.datetime.fromtimestamp(int(a)).strftime('%Y-%m-%d %H:%M:%S')
    return b

def MinDistance(a,j):
    distance1 = sqrt(pow((a['Long'][1] - a['Long'][0]), 2) + pow((a['Latt'][1] - a['Latt'][0]), 2))
    # print(distance1)
    for i in range(2, len(a['UnixTime'])):
        distance2 = sqrt(pow((a['Long'][i] - a['Long'][i-1]), 2) + pow((a['Latt'][i] - a['Latt'][i-1]), 2))
        if (distance2 < distance1):
            # print(distance2)
            distance1 = distance2
    print("Khoang cach min cua con %s là: " % label[j] + str(distance1) + " voi time là: "+ a['Time'][i]+" va "+ a['Time'][i-1])

def set_Index(a):
    count = []
    for i in range(0,len(a['UnixTime'])):
        count.append(i)
    a.index = count

if __name__ == '__main__':
    file = "ZebraBotswana.txt"

    df = pd.read_csv(file, delimiter=",")
    # print(df)
    # print(len(df['UnixTime']))

    df.sort_values('UnixTime', inplace=True)

    # print(df)
    time = []
    for i in range(0, len(df['UnixTime'])):
        time.append(ConvertTime(df['UnixTime'][i]))

    # print(time)
    df['Time'] = pd.Series(time, index=df.index)
    # print(df)

    label = []

    for i in range(0, len(df['Animal'])):
        if df['Animal'][i] not in label:
            label.append(df['Animal'][i])
    # print(label)
    # print(len(label))
    # print(label[6])

    a0 = df.query("Animal == '%s'" % label[0])
    a1 = df.query("Animal == '%s'" % label[1])
    a2 = df.query("Animal == '%s'" % label[2])
    a3 = df.query("Animal == '%s'" % label[3])
    a4 = df.query("Animal == '%s'" % label[4])
    a5 = df.query("Animal == '%s'" % label[5])
    a6 = df.query("Animal == '%s'" % label[6])

    # data = []
    # with open("output.txt", "w", encoding='utf-8') as file:
    #     for i in range(0,len(a0['Time'])):
    #         file.write(str(a0['UnixTime'][i])+"\t"+str(a0['Time'][i])+"\n")

    plt.plot(a0['Long'], a0['Latt'], '#16a085', linewidth=0.5, label=label[0])
    plt.plot(a1['Long'], a1['Latt'], '#c0392b', linewidth=0.5, label=label[1])
    plt.plot(a2['Long'], a2['Latt'], '#3498db', linewidth=0.5, label=label[2])
    plt.plot(a3['Long'], a3['Latt'], '#363636', linewidth=0.5, label=label[3])
    plt.plot(a4['Long'], a4['Latt'], '#0000FF', linewidth=0.5, label=label[4])
    plt.plot(a5['Long'], a5['Latt'], '#FFFF00', linewidth=0.5, label=label[5])
    plt.plot(a6['Long'], a6['Latt'], '#FF00FF', linewidth=0.5, label=label[6])

    plt.legend(loc=1)
    # plt.title("Number of animals each year")
    # plt.xlabel("Years")
    # plt.xticks(a, years)
    # plt.show()

    set_Index(a0)
    MinDistance(a0, 0)
    set_Index(a1)
    MinDistance(a1, 1)
    set_Index(a2)
    MinDistance(a2, 2)
    set_Index(a3)
    MinDistance(a3, 3)
    set_Index(a4)
    MinDistance(a4, 4)
    set_Index(a5)
    MinDistance(a5, 5)
    set_Index(a6)
    MinDistance(a6, 6)

    plt.show()




