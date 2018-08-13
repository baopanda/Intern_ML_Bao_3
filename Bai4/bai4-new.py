import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from threading import Thread
from scipy.spatial.distance import cdist, euclidean
from datetime import datetime
import math

result = []


class MyThread(Thread):
    def __init__(self, name, group):
        super(MyThread, self).__init__()
        self.name = name
        self.group = group

    def run(self):
        print("Bat dau chay thread %s..." % (self.name))
        global result
        x = toList(self.group)
        d1, d2, m = solution(x, x)
        result.append([self.name, m,str(d1),str(d2)])
        print("Xong thread %s!" % (self.name))

def ConvertTime(a):
    # b = datetime.fromtimestamp(int(a)).strftime('%Y-%m-%d %H:%M:%S')
    b = datetime.fromtimestamp(int(a)).strftime('%d-%m-%Y')
    return b


def toList(group):
    a = list()
    # group = set_Index(group)
    # x = group["Longtitude"].loc[0]
    # y = group["Latitude"].loc[0]
    # t1 = group["Time"].loc[0]
    # a.append([x, y, t1])
    for i, row in group.iterrows():
        t2 = row["Time"]
        x = row["Longtitude"]
        y = row["Latitude"]
        a.append([x, y, t2])
    return a


def sub_time(t1, t2):
    date_format = "%d-%m-%Y"
    d1 = datetime.strptime(t1, date_format)
    d2 = datetime.strptime(t2, date_format)
    return abs(d1 - d2)

def dist(p1, p2):
    return euclidean(p1[:2], p2[:2])


def solution(x, y):
    ax = sorted(x, key=lambda x: x[0])  # Presorting x-wise
    ay = sorted(y, key=lambda y: y[1])  # Presorting y-wise
    d1, d2, mi = closest_pair(ax, ay)  # Recursive D&C function
    return d1, d2, mi


def min(d1x, d2x, x, d1y, d2y, y):
    if (x < y):
        return d1x, d2x, x
    else:
        return d1y, d2y, y

def set_Index(a):
    count = []
    for i in range(0,len(a['UnixTime'])):
        count.append(i)
    a.index = count
    return a


def stripClosest(strip, d1, d2, mi):
    i = 0
    while (i < len(strip)):
        j = i + 1
        while (j < len(strip) and strip[j][1] - strip[i][1] < mi):
            if (dist(strip[i], strip[j]) < mi and sub_time(strip[i][2], strip[j][2]).days >= 1):
                mi = dist(strip[i], strip[j])
                d1 = strip[i][2]
                d2 = strip[j][2]
            j += 1
        i += 1
    return d1, d2, mi


def closest_pair(ax, ay):
    ln_ax = len(ax)  # It's quicker to assign variable
    if ln_ax <= 3:
        return brute(ax)  # A call to bruteforce comparison
    mid = ln_ax // 2  # Division without remainder, need int
    Qx = ax[:mid]  # Two-part split
    Rx = ax[mid:]
    # Determine midpoint on x-axis
    midpoint = ax[mid][0]
    Qy = []
    Ry = []
    for x in ay:  # split ay into 2 arrays using midpoint
        if x[0] <= midpoint:
            Qy.append(x)
        else:
            Ry.append(x)
    # Call recursively both arrays after split
    d1l, d2l, mi1 = closest_pair(Qx, Qy)
    d1r, d2r, mi2 = closest_pair(Rx, Ry)
    # Determine smaller distance between points of 2 arrays
    d1, d2, mi = min(d1l, d2l, mi1, d1r, d2r, mi2)
    # return min(d1l,d2l,mi1,d1r,d2r,mi2)
    strip = []
    for i in range(ln_ax - 1):
        if (abs(ay[i][0] - midpoint) < mi):
            strip.append(ay[i])
    d11, d22, mi2 = stripClosest(strip, d1, d2, mi)
    return min(d1, d2, mi, d11, d22, mi2)


def brute(ax):
    mi = 9999
    d1 = ax[0][2]
    d2 = ax[1][2]

    for i in range(len(ax) - 1):
        for j in range(i + 1, len(ax)):
            if (sub_time(ax[i][2],ax[j][2]).days >= 1 and dist(ax[i], ax[j]) < mi):
                mi = dist(ax[i], ax[j])
                d1 = ax[i][2]
                d2 = ax[j][2]
    return d1, d2, mi


if __name__ == "__main__":
    df = pd.read_csv("ZebraBotswana.txt")
    df.columns = ["UnixTime", "Longtitude", "Latitude", "Id"]

    time = []
    for i in range(0, len(df['UnixTime'])):
        time.append(ConvertTime(df['UnixTime'][i]))

    df['Time'] = pd.Series(time, index=df.index)


    print(df)
    df = df.groupby("Id")[["UnixTime", "Longtitude", "Latitude","Time"]]
    fig, ax = plt.subplots(figsize=(10, 5))
    plt.xlabel("Longtitude")
    plt.ylabel("Latitude")
    color = ["r-", "g-", "b-", "c-", "y-", "k-", "m-"]

    listThread = list()
    i = 0
    for name, group in df:
        plt.plot(group["Longtitude"], group["Latitude"], color[i], linewidth=0.5, label=name)
        i += 1
        thread = MyThread(name, group)
        listThread.append(thread)
        thread.start()

    for t in listThread:
        t.join()
    for i in result:
        print("Con ngua "+ str(i[0])+" co khoang cach min la: "+ str(i[1])+ " giưa ngay " + str(i[2])+ " va ngay "+str(i[3]))
    ax.legend(loc='upper right')
    # plt.savefig("plot.jpg")
    # plt.show()
