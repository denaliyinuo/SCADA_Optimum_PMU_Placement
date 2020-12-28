import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# # IEEE 14
# file_name = 'ieee_14'
# pmu = [7]
# n = 3
# df_length = 14

# # IEEE 30
file_name = 'ieee_30'
pmu = [9, 12, 25]
n = 7
df_length = 30

# # New England 39
# file_name = 'new_england_39'
# pmu = [2, 6, 10, 19, 20, 22, 23, 25, 29]
# n = 4
# df_length = 39


test_buses = []
initial = []
final = []
change = []


for i in range(n):
    test_buses.append(i + 1)
    initial.append(i + 1)
    change.append(i + 1)
    final.append(df_length - i)

final.sort()

test_buses[n - 1] = test_buses[n - 2]

print(test_buses)


def create_test_buses(n, test_buses, pmu, df):

    for k in range(n - 1, -1, -1):

        # print(test_buses[k])
        # print(test_buses[k])
        if test_buses[k] == final[k]:
            # print('entered1')
            s = 1
            for col in range(n):
                # print('entered2')
                if test_buses[col] == final[col]:
                    # s = s + 1

                    # print('entered2 col', col)
                    # print('entered2 test_bus', test_buses)
                    # print('entered2 test_bus[col]', test_buses[col])
                    # print('entered2 change[col]', change[col])
                    # print('entered2 change', change)

                    # change[col] = change[col] + 1
                    # test_buses[col] = change[col]

                    # test_buses[col - 1] = change[col - 1]
                    # change[col - 1] = test_buses[col - 1]

                    test_buses[col - 1] = test_buses[col - 1] + 1
                    test_buses[col] = test_buses[col - 1]

                    change[col - 1] = change[col - 1] + 1
                    change[col] = change[col - 1]

                    # test_buses[col] = change[col - 1] + 1
                    # change[col] = test_buses[col - 1] + 1
                    # print('entered2 col', col)
                    # print('entered2 test_bus', test_buses)
                    # print('entered2 test_bus[col]', test_buses[col])
                    # print('entered2 change[col]', change[col])
                    # print('entered2 change', change)

                    if col == n - 1:
                        test_buses[col] = test_buses[col - 1] + 1
                        # print('return test buses1')
                        return test_buses

            # print(test_buses)

            if test_buses[k - 1] == final[k - 1]:
                #     print('entered')
                #     print(test_buses)
                pass
            #     test_buses[k - 1] = test_buses[k - 2] + 1
            #     change[k - 1] = test_buses[k - 2] + 1
            #     test_buses[k] = change[k - 1] + 2
            #     change[k] = test_buses[k - 1] + 2
            #     print(change)
            else:

                change[k - 1] = change[k - 1] + 1
                change[k] = change[k] + 1
                # test_buses[k - 1] = change[k - 1]
                test_buses[k] = change[k]
                # test_buses[k] = 1

            while test_buses[k] in pmu:
                test_buses[k] = test_buses[k] + 1
            # if k == df:
            #     test_buses[k + 1] = 1

            #     # for i in range(1,n):
            #     #     if

            # else:
            #     test_buses[k + 1] = test_buses[k + 1] + 1
            #     break
        else:
            test_buses[k] = test_buses[k] + 1
            # print(test_buses[k])
            while test_buses[k] in pmu:
                test_buses[k] = test_buses[k] + 1

            break
            # if k == n-1
            #     test_buses[k+1] =

    return test_buses


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# pmu = [2, 6, 10, 19, 20, 22, 23, 25, 29]

# test_buses = [1, 3, 5, 7]
# test_buses = [9, 13, 14, 17]


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df

# import files


path = '/Users/nathanoliver/Desktop/Python/SCADA/csv/01_files_after_cleaning/' + \
    file_name + '.csv'

df = read_file(path)


visible_buses = []

for i in range(df_length):
    visible_buses.append(0)

print(visible_buses)

print(df)


# program to determine visible buses

def check_visibility(df, visible_buses, pmu):
    for i in range(len(df)):
        bus1 = df.iloc[i, 0]
        bus2 = df.iloc[i, 1]

        if bus1 in pmu:
            visible_buses[bus2 - 1] = 1
            visible_buses[bus1 - 1] = 1
        if bus2 in pmu:
            visible_buses[bus1 - 1] = 1
            visible_buses[bus2 - 1] = 1

    return visible_buses


visible_buses = check_visibility(df, visible_buses, pmu)


# visible_buses_new = check_visibility(df, visible_buses, test_buses)

# print(visible_buses)

y = 0

while test_buses[0] < ((df_length) - (n - 1)):

    y = y + 1
    x = visible_buses.copy()
    # print(test_buses)
    test_buses = create_test_buses(n, test_buses, pmu, df)
    # print(test_buses)
    # print(x)
    visible_buses_new = check_visibility(df, x, test_buses)
    # print(visible_buses_new)

    if sum(visible_buses_new) == df_length:
        print('result: ', test_buses)

    if y == 10000:
        y = 0
        print()
        print('every 10000: ', test_buses)
        print()

print()
print('*** Complete ***')
print()
