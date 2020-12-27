import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pmu = [2, 6, 10, 19, 20, 22, 23, 25, 29]

n = 3

df = 39

# test_buses = [1, 1, 1, 1]

test_buses = []

for i in range(n):
    test_buses.append(1)

print(test_buses)


def create_test_buses(n, test_buses, pmu, df):

    for k in range(n):

        if test_buses[k] == df:
            test_buses[k] = 1

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

            while test_buses[k] in pmu:
                test_buses[k] = test_buses[k] + 1

            break
            # if k == n-1
            #     test_buses[k+1] =

    return test_buses


for i in range((df - len(pmu))**n):
    test_buses = create_test_buses(n, test_buses, pmu, df)
    print(test_buses)
