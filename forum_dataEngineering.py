import pandas as pd

df = pd.DataFrame({'Nilai': [85, 90, 78]}, index=['Andi', 'Budi', 'Cici'])

# Menggunakan loc
print(df.loc['Andi':'Budi'])

# Menggunakan iloc
print(df.iloc[0:2])