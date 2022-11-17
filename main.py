import pandas as pd
from data_save import salvaDados

#consultando url e transformando resultado em DataFrame
df = pd.read_json('https://swapi.dev/api/films/?format=json')
df.drop('count', axis=1, inplace=True)
df.drop('next', axis=1, inplace=True)
df.drop('previous', axis=1, inplace=True)
df = pd.DataFrame(df['results'].values.tolist(), index=df.index)

df2 = df['planets'].to_string()
df2 = df2.replace("'", '')
df2 = df2.replace("[", '')
df2 = df2.replace("]", '')
df.drop('planets', axis=1, inplace=True)
df.insert(column="planets", value=df2, loc=6)

df3 = df['characters'].to_string()
df3 = df3.replace("'", '')
df3 = df3.replace("[", '')
df3 = df3.replace("]", '')
df.drop('characters', axis=1, inplace=True)
df.insert(column="characters", value=df3, loc=7)

df4 = df['starships'].to_string()
df4 = df4.replace("'", '')
df4 = df4.replace("[", '')
df4 = df4.replace("]", '')
df.drop('starships', axis=1, inplace=True)
df.insert(column="starships", value=df4, loc=8)

df5 = df['vehicles'].to_string()
df5 = df5.replace("'", '')
df5 = df5.replace("[", '')
df5 = df5.replace("]", '')
df.drop('vehicles', axis=1, inplace=True)
df.insert(column="vehicles", value=df5, loc=9)

df6 = df['species'].to_string()
df6 = df6.replace("'", '')
df6 = df6.replace("[", '')
df6 = df6.replace("]", '')
df.drop('species', axis=1, inplace=True)
df.insert(column="species", value=df6, loc=10)

salvaDados(df)

print(df)