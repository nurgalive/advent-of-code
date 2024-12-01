"""
Calculate difference between sorted left and right part.
"""


import pandas

df = pandas.read_csv("input.txt", delim_whitespace=True, header=None)
# print(df[0])

column1 = sorted(list(df[0]))
column2 = sorted(list(df[1]))
# print(column1)

res = 0
for val1, val2 in zip(column1, column2):
    # print(val1, val2)
    res += abs(val1 - val2)

print(res)
