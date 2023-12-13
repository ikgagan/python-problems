import pandas as pd
import plotly.express as px

file_path = "pokemon.csv" 
data = pd.read_csv(file_path)
fig = px.scatter(data,
                 x='Year',
                 y='Average Score',
                 size='Units Sold (in millions)',
                 color='First Entry in Generation',
                 hover_name='Game',
                 title='Pokémon Sales Data')
fig.show()

top_5_games = data[data['First Entry in Generation'] == 'Yes'].nlargest(5, 'Units Sold (in millions)')[['Game', 'Year', 'Units Sold (in millions)']]
top_5_games.set_index('Game', inplace=True)

print(top_5_games)

non_first_entry_top_5 = data[data['First Entry in Generation'] == 'No'].nlargest(5, 'Units Sold (in millions)')[['Game', 'Year', 'Units Sold (in millions)']]
non_first_entry_top_5.set_index('Game', inplace=True)

print(non_first_entry_top_5)

first_entry_units_sold = data[data['First Entry in Generation'] == 'Yes']['Units Sold (in millions)'].sum()

non_first_entry_units_sold = data[data['First Entry in Generation'] == 'No']['Units Sold (in millions)'].sum()

print("Total units sold for games which are 'First Entry in Generation':", first_entry_units_sold, "million")
print("Total units sold for games which are not 'First Entry in Generation':", non_first_entry_units_sold, "million")