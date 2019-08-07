import numpy as np
import datetime
import sys

# calculate correlation coefficients
def calc_r(x, y):

    if len(x) != len(y):
        print("not equal length data")
        sys.exit()

    sum_sin = 0
    sum_cos = 0
    for i in x:
        sum_sin += np.sin(np.radians(i))
        sum_cos += np.cos(np.radians(i))
    S1 = sum_sin
    C1 = sum_cos
    sum_sin = 0
    sum_cos = 0
    # print("S1:", S1)
    # print("C1:", C1)

    for i in y:
        sum_sin += np.sin(np.radians(i))
        sum_cos += np.cos(np.radians(i))
    S2 = sum_sin
    C2 = sum_cos
    # print("S2:", S2)
    # print("C2:", C2)

    if C1 < 0:
        cent1 = np.arctan(S1 / C1) + np.pi
    elif S1 < 0:
        cent1 = np.arctan(S1 / C1) + 2 * np.pi
    else:
        cent1 = np.arctan(S1 / C1)

    if C2 < 0:
        cent2 = np.arctan(S2 / C2) + np.pi
    elif S2 < 0:
        cent2 = np.arctan(S2 / C2) + 2 * np.pi
    else:
        cent2 = np.arctan(S2 / C2)
    # print("Average Rotation(rad)", cent1, cent2)
    # print("Average Rotation(deg)", np.rad2deg(cent1), np.rad2deg(cent2))

    a = 0.0
    b = 0.0
    for i in range(len(x)):
        a += np.sin(np.radians(x[i]) - cent1) * np.sin(np.radians(y[i]) - cent2)
        b += (np.sin(np.radians(x[i]) - cent1) ** 2) * (np.sin(np.radians(y[i]) - cent2) ** 2)
    r = a / np.sqrt(b)

    return r

# transform date data to angle data
def convert_rad(x):
    ar = []
    for idx, (i, j) in enumerate(x):
        a = datetime.date(2011 + idx, 1, 1)
        b = datetime.date(2011 + idx, i, j)
        c = (b - a).days
        c = c / (datetime.date(2011 + idx, 12, 31)-datetime.date(2011 + idx, 1, 1)).days * 360
        ar.append(c)
    return ar


tokyo = np.array([[3, 28], [3, 31], [3, 16], [3, 25], [3, 23], [3, 21], [3, 21], [3, 17], [3, 26]])
sapporo = np.array([[5, 7], [5, 1], [5, 13], [4, 29], [4, 22], [4, 25], [4, 28], [4, 26], [5, 3]])

conv_tokyo = convert_rad(tokyo)
conv_sapporo = convert_rad(sapporo)
# print(conv_tokyo, conv_sapporo)
r = calc_r(conv_tokyo, conv_sapporo)
print("r =", r)
print("nr^2 =", len(conv_sapporo)*(r**2))
