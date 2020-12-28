import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df

# import files


# file_name = 'ieee_14'
# file_name = 'ieee_30'
file_name = 'new_england_39'


path = '/Users/nathanoliver/Desktop/Python/SCADA/csv/01_files_after_cleaning/' + \
    file_name + '.csv'

df = read_file(path)

# create list of buses

bus = []

for i in range(len(df)):
    bus1 = df.iloc[i, 0]
    bus2 = df.iloc[i, 1]

    if bus1 not in bus:
        bus.append(bus1)
    if bus2 not in bus:
        bus.append(bus2)

bus.sort()


# create connectivity matrix

connect = np.zeros((len(bus), len(bus)))

for i in range(len(df)):
    bus1 = df.iloc[i, 0]
    bus2 = df.iloc[i, 1]

    connect[bus1 - 1, bus2 - 1] = 1
    connect[bus2 - 1, bus1 - 1] = 1


# determine number of branches for each node

branch = np.sum(connect, axis=0)
branch_original = branch.copy()


pmu = []


# determine which buses receive PMU

# first place PMUs at buses adjacent to buses with only one branch

for j in range(len(branch)):

    n = branch[j]
    # print('')
    # print('branch', n)
    if n == 1:
        for i in range(len(df)):

            bus1 = df.iloc[i, 0]
            bus2 = df.iloc[i, 1]

            if bus1 == j + 1:
                # print('entered bus 1')
                # print('bus1', bus1)
                # print('bus2', bus2)
                # print('bus with single branch', j + 1)
                pmu.append(bus2)
                connect[bus1 - 1, bus2 - 1] = 0
                connect[bus2 - 1, bus1 - 1] = 0
                branch[bus2 - 1] = 0
                branch[bus1 - 1] = branch[bus1 - 1] - 1
            if bus2 == j + 1:
                # print('entered bus 2')
                # print('bus1', bus1)
                # print('bus2', bus2)
                # print('bus with single branch', j + 1)
                pmu.append(bus1)
                connect[bus1 - 1, bus2 - 1] = 0
                connect[bus2 - 1, bus1 - 1] = 0
                branch[bus1 - 1] = 0
                branch[bus2 - 1] = branch[bus2 - 1] - 1


def reduce_branches(branch, max_bus):

    branch[max_bus - 1] = 0

    for i in range(len(branch)):
        bus1 = df.iloc[i, 0]
        bus2 = df.iloc[i, 1]

        if bus1 == max_bus:
            if branch[bus2 - 1] > 0:
                # branch[bus2 - 1] = branch[bus2 - 1] - 1
                branch[bus2 - 1] = 0
        if bus2 == n:
            if branch[bus1 - 1] > 0:
                # branch[bus1 - 1] = branch[bus1 - 1] - 1
                branch[bus2 - 1] = 0

#     for j in range(len(pmu)):
#         n = pmu[j]

#         for i in range(len(df)):

#             bus1 = df.iloc[i, 0]
#             bus2 = df.iloc[i, 1]

#             if bus1 == n:
#                 branch[bus1 - 1] = branch[bus1 - 1] - 1

#             if bus2 == n:
#                 branch[bus2 - 1] = branch[bus2 - 1] - 1

    return branch


print(branch)
print(pmu)

# reduce_branches(branch, pmu, connect)


# sum_branch = np.sum(branch, axis=0)


# while sum_branch > 0:
#     max_bus = np.argmax(branch)

#     pmu.append(max_bus + 1)

#     branch = reduce_branches(branch, max_bus + 1)

#     print(branch)

#     sum_branch = np.sum(branch, axis=0)

# print(pmu)


# print(len(pmu))
