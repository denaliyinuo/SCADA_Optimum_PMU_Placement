import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_name = 'ieee_30'

pmu = [9, 12, 25]

n = 7

df_length = 30

# test_buses = [1, 1, 1, 1]

test_buses = []

for i in range(n):
    test_buses.append(i + 1)

print(test_buses)


def create_test_buses(n, test_buses, pmu, df):

    for k in range(n):

        if test_buses[k] == df_length:
            test_buses[k] = 1

            while test_buses[k] in pmu:
                test_buses[k] = test_buses[k] + 1
        else:
            test_buses[k] = test_buses[k] + 1

            while test_buses[k] in pmu:
                test_buses[k] = test_buses[k] + 1
            break
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


for i in range((df_length - len(pmu))**n):
    x = visible_buses.copy()
    # print(test_buses)
    test_buses = create_test_buses(n, test_buses, pmu, df)
    # print(test_buses)
    # print(x)
    visible_buses_new = check_visibility(df, x, test_buses)
    # print(visible_buses_new)

    if sum(visible_buses_new) == df_length:
        print(test_buses)
