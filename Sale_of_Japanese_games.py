import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


games = pd.read_csv('games.csv')


games.isna().sum()


games = games.dropna()


games['Year'] = games['Year'].astype('int')


games.describe()


# Показывает моду
stats.mode(games.Year)


sns.countplot(games.Year)
sns.set(rc={'figure.figsize':(20,20)})
plt.title("Sale of games by years", fontsize=20)
plt.xlabel('Year', fontsize=20)
plt.ylabel('Count', fontsize=20)
plt.tick_params(axis='x', which='major', labelsize=17, rotation=45)
plt.tick_params(axis='y', labelsize=17)


games.query('Year > 2007').shape


games.groupby('Platform').agg('count')


games.Platform.value_counts(normalize=True)*100


games.groupby('Publisher').agg('count')


games.Publisher.value_counts(normalize=True)


stats.mode(games.Publisher)


games.Publisher.value_counts()


games.query('Publisher == "Nintendo"').describe()


sns.boxplot(x='Genre', y='JP_Sales', data=games)
sns.set(rc={'figure.figsize':(20,20)})
plt.tick_params(axis='x', which='major', labelsize=17, rotation=45)
plt.tick_params(axis='y', labelsize=17)
plt.title("Japan games genre", fontsize=20)
plt.xlabel('Genre', fontsize=20)
plt.ylabel('Sales', fontsize=20)


nintendo_games = games.query('Publisher == "Nintendo"')


sns.boxplot(x='Genre', y='JP_Sales', data=nintendo_games)
sns.set(rc={'figure.figsize':(20,20)})
plt.title("Nintendo games", fontsize=20)
plt.xlabel('Genre', fontsize=20)
plt.ylabel('Sales', fontsize=20)


genre_game = games.query("Genre in ('Fighting', 'Simulation', 'Platform', 'Racing', 'Sports')").groupby('Global_Sales').agg('sum')


sns.lineplot(data=genre_game, x="Year", y="Rank")


genre_game.head()


genre_game_2 = games.query("Genre in ('Fighting', 'Simulation', 'Platform', 'Racing', 'Sports')").groupby(['Genre', 'Year']).agg('sum')


genre_game_2.head()


sns.lineplot(data=genre_game_2, x="Year", y="Global_Sales")

