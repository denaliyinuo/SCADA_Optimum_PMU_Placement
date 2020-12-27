import pandas as pd
import matplotlib.pyplot as plt


def read_file(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df

# import files

file_name = 'ieee_30'

path = '/Users/nathanoliver/Desktop/Python/SCADA/csv/00_files_before_cleaning/' + file_name + '.csv'

df = read_file(path)

# define new dataframe for grid test case

column_names = ['bus_1', 'bus_2']

df1 = pd.DataFrame(columns=column_names)

# clean test case data, form branches into two columns, each with start and end bus

for i in range(len(df)):
    split = df.iloc[i, 0].split(' ')
    df1.loc[i, 'bus_1'] = split[0]
    df1.loc[i, 'bus_2'] = split[1]

print(df1)

df1.drop

df1.to_csv(
    '/Users/nathanoliver/Desktop/Python/SCADA/csv/01_files_after_cleaning/' + file_name + '.csv', index=False)
