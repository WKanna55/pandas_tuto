import pandas as pd

"""
========================================================
                LOADING DATA IN PANDAS
========================================================
"""

"""Load csv"""
df = pd.read_csv('pokemon_data.csv')
#print(df.tail(3))
#print(df.head(5))

"""Load xlsx"""
df_xlsx = pd.read_excel('pokemon_data.xlsx')

#print(df_xlsx.head(5))
#print(df_xlsx.tail(2))

"""Load txt"""
df_txt = pd.read_csv('pokemon_data.txt', delimiter='\t')
#df_txt = pd.read_csv('pokemon_data.txt', sep='\t')
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
#columna001 = 'Name'
#columna002 = 'HP'
#print(f"Leendo la columna {columna001}:\n{df[columna001]}")
#print(f"Leendo la columna {columna001} delimitado de 0 a 5:\n{df[columna001][0:5]}")
#print(f"Leendo la columna {columna001} de otra manera:\n{df.Name}") # no funcionan para nombres de 2 palabras o mas
#print(f"Leendo columnas {columna001} y {columna002}:\n{df[[columna001, columna002]]}")

"""leer por fila"""
#print(f"Leer fila 1:\n{df.iloc[1]}")
#print(f"Leer fila 1 a 3:\n{df.iloc[1:4]}")

"""Datos por columna pero iterado"""
#for index, row in df.iterrows():
#  print(index, row['Name'])

"""leer una posicion especifica (fila - columna)"""
#print(f"Leer posicion especifica 2, 1:\n{df.iloc[2,1]}")
#print(f"Leer posicion por coincidencia textual en columna:\n{ df.loc[df['Type 1'] == 'Fire'] }") #optimo si solo filtra un valor o pocos

"""
========================================================
                Sorting / Describing data
========================================================
"""

"""Sacar datos estadisticos (medida de tendencia central, dispersion)"""
#print(f"Datos estadisticos:\n{df.describe()}")

"""Ordenamiento Ascendiente por columna(s)"""
#print(f"Ordenar datos por Name:\n{df.sort_values('Name')}")
#print(f"Ordenar datos por Type 1 y HP:\n{df.sort_values(['Type 1', 'HP'])}")

"""Ordenamiento Descendente por columna(s)"""
#print(f"Ordenar datos por Name:\n{df.sort_values('Name', ascending=False)}")
#print(f"Ordenar datos por Type 1 y HP:\n{df.sort_values(['Type 1', 'HP'], ascending=False)}")

"""Ordenamiento por columnas ascendiente combinado con descendiente"""
#print(f"Ordenar datos por Type 1 y HP - ascendiente y descendiente respectivamente:\n{df.sort_values(['Type 1', 'HP'], ascending=[1,0])}")

"""
========================================================
              Making changes to the data
========================================================
"""

"""Agregar una columna 'Total' al df"""
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
#print(df.head(5))

# un poco peligroso mejor especificar
#df['Total'] = df.iloc[:, 4:10].sum(axis=1) #suma de columnas 4 al 9 de manera (axis=1) horizontal
#print(df.head(5))

"""Eliminar columna(s)"""
#df = df.drop(columns=['Total'])
#print(df.head(5))

"""Reordenar las columnas para que Total no sea la ultima"""
#cols = list(df.columns.values)
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
#print(df.head(5))

"""
========================================================
    Saving our Data (Exporting into desired format)
========================================================
"""

"""guardar en csv"""
#df.to_csv('modified.csv') # con indices
#df.to_csv('modified.csv', index=False) # sin indices

"""guardar en excel"""
#df.to_excel('modified.xlsx', index=False) # sin indices

"""guardar en txt con delimitador/separador """
#df.to_csv('modified.txt', index=False, sep='\t') # sin indices, con separador tab

"""
========================================================
                    Filtering Data 
========================================================
"""

"""buscando coincidencias especificando textualmente una dato por columna(s) """
""" Condicionales & (and), | (or), == (igual que), > (mayor que), < (menor que)"""
#print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])
#print(df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')])
#print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)])

#new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] # mantiene indices anteriores
#new_df = new_df.reset_index(drop=True) # se reinician los indices, con drop borramos los indices anteriores(se conservan sino) 
#new_df.reset_index(drop=True, inplace=True) # con inplace no es necesario reasignarlo
#new_df.to_csv('filtered.csv')


"""Buscar por columna(s) que contengan cierto texto en su contenido"""
""" ojo: ! en pandas es ~"""
""" ojo: se puede usar Regex"""
#print(df.loc[df['Name'].str.contains('Mega')]) # nombres que contengan Mega
#print(df.loc[~df['Name'].str.contains('Mega')]) # nombres que no contengan Mega

#import re
#print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]) # uso regex para filtrar el tipo por fire o grass
#print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I,regex=True)]) # uso de flag para ignorar capitalizacion

#print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I,regex=True)]) # que el name contenga pi al inicio


"""
========================================================
                  Conditional Changes
========================================================
"""

"""Cambiar un dato por otro segun todas las coincidencias de una columna"""
#df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer' #cambiar 'Fire' por 'Flamer'
#print(df)

#df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True #Todos los pokemones Fire son legendarios
#print(df)

"""Cambiar multiples parametros al mismo tiempo"""
#df = pd.read_csv('modified.csv')

#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['TEST 1', 'TEST 2']
#print(df)

"""
========================================================
              Aggregate Statistics (Groupby)
========================================================
"""

#df = pd.read_csv('modified.csv')

"""Agrupar y hacer operaciones"""
"""Promedio"""
#print(df.groupby(['Type 1']).mean(numeric_only=True).sort_values('Defense', ascending=False)) # agrupados por Type 1 

"""Suma"""
#print(df.groupby(['Type 1']).sum(numeric_only=True)) # sumar valores de Type 1

"""Contar"""
#print(df.groupby(['Type 1']).count()) # Contar todas las filas segun Type 1

#df['count'] = 1
#print(df.groupby(['Type 1']).count()['count']) # contar pokemones por tipo 1
#print(df.groupby(['Type 1', 'Type 2']).count()['count']) # contar con agrupacion de 2 columnas



"""
========================================================
            Working with large amounts of data
========================================================
"""

#new_df = pd.DataFrame(columns=df.columns)
#
#for df in pd.read_csv('modified.csv', chunksize=5):
#  results = df.groupby(['Type 1']).count()
#
#  new_df = pd.concat([new_df, results])
#  print('Chunk df')
#  print(new_df)
