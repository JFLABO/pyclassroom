import pandas as pd

df_ab = pd.DataFrame({'a': ['a_1', 'a_2', 'a_3'], 'b': ['b_1', 'b_2', 'b_3']})
df_ac = pd.DataFrame({'a': ['a_1', 'a_2', 'a_4'], 'c': ['c_1', 'c_2', 'c_4']})

#print(df_ab)
#      a    b
# 0  a_1  b_1
# 1  a_2  b_2
# 2  a_3  b_3

print(df_ac)
#      a    c
# 0  a_1  c_1
# 1  a_2  c_2
# 2  a_4  c_4
df = pd.read_csv('./data/lunch_box.csv', sep=',')
df.head(3)
df.plot()
df.groupby(['month', 'period'])['sales'].sum()