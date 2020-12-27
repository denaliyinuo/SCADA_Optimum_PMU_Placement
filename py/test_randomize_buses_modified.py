import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pmu = []

n = 4

df_length = 10

# test_buses = [1, 1, 1, 1]

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

print(final)

print(test_buses)


def create_test_buses(n, test_buses, pmu, df_length):

    for k in range(n - 1, -1, -1):

        # print(test_buses[k])
        # print(test_buses[k])
        if test_buses[k] == final[k]:
            print('entered1')
            s = 1
            for col in range(n - 1, -1, -1):
                print('entered2')
                if test_buses[col] == final[col]:
                    # s = s + 1
                    print(test_buses[col])
                    print(test_buses)

                    test_buses[col] = change[col]

                    test_buses[col] = change[col - 1] + 1
                    change[col] = test_buses[col - 1] + 1

            print(test_buses)

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


for i in range(29):
    test_buses = create_test_buses(n, test_buses, pmu, df_length)
    print('returned', test_buses)
