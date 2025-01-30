import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = ('/Downloads/pokedata.csv')

pokemon = pd.read_csv(filepath)

pokemon.rename(columns={"#": "num", "Name" : "name", "Type 1" : "type1",
                                "Type 2" : "type2", "Total" : "total", "HP" : "hp", "Attack" : "atk",
                                "Defense" : "def", "Sp. Atk" : "sp_atk", "Sp. Def" : "sp_def",
                                "Speed" : "speed", "Generation" : "gen", "Legendary" : "legendary"}, inplace = True)
pokemon.drop_duplicates('num', keep='first', inplace=True)
pokemon['type2'].fillna(value = 'none', inplace = True)


print(pokemon.head())

x = pokemon.drop('name', axis = 1)
y = pokemon.name

print(x.head(5))
print(y.head(5))

#type distribution!

count = x['type1'].value_counts().sort_index()
print(count)

plt.figure()
plt.bar(count.index, count.values)
plt.title('type distribution')
plt.show()

