"""
Calculate a total similarity score by adding up each number in the left list after multiplying it
by the number of times that number appears in the right list.

31 (9 + 4 + 0 + 0 + 9 + 9)

3   4
4   3
2   5
1   3
3   9
3   3
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
    value_counts = df[1].value_counts()
    count = value_counts.get(val1, 0)
    # print(f"Value '{val1}' is presented '{count}' times in col_2")
    res += count * val1

print(res)
