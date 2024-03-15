import pandas as pd

# 读取第一个Excel文件
df1 = pd.read_excel('C:/Users/Epiphany/Desktop/sunday.xlsx')

# 读取第二个Excel文件
df2 = pd.read_excel('C:/Users/Epiphany/Desktop/total.xlsx')

# 在第二个DataFrame中找出与第一个Excel文件中的名字相匹配的数据
matched_df = df2[df2['你的姓名'].isin(df1['姓名：'])]

# 将匹配的数据保存到新的Excel文件中
matched_df.to_excel('matched_data.xlsx', index=False)