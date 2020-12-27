import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pmu = [2, 6, 10, 19, 20, 22, 23, 25, 29]

n = 3

df_length = 39


# test_buses = [1, 3, 5, 7]
test_buses = [9, 13, 14, 17]


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df

# import files


path = '/Users/nathanoliver/Desktop/Python/SCADA/csv/01_files_after_cleaning/new_england_39.csv'

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

print(visible_buses)

visible_buses = check_visibility(df, visible_buses, test_buses)

print(visible_buses)
