import pandas as pd

"""
========================================================
                LOADING DATA IN PANDAS
========================================================
"""

df = pd.read_csv('pokemon_data.csv')
#print(df.tail(3))
#print(df.head(5))

df_xlsx = pd.read_excel('pokemon_data.xlsx')

#print(df_xlsx.head(5))
#print(df_xlsx.tail(2))

df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')

#print(df_txt.head(5))
#print(df_txt.tail(2))


"""
========================================================
                READING DATA IN PANDAS
========================================================
"""

"""Leer primeras filas 5"""
#print(df.head(5))

"""leer ultimas filas 3"""
#print(df.tail(3))

"""leer encabezados"""
#print(df.columns)

"""leer por columna"""
#print(df['Name'])
#print(df['Name', 'Type 1'].head(2))
#print(df['Name'].tail(2))


"""leer encabezados"""



"""leer encabezados"""



"""leer encabezados"""



"""leer encabezados"""