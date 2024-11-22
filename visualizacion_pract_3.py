import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('movies_clean.csv')

#Gráfica de Bigote, duración agrupada por los 20 países con más peliculas
#Filtraré los 20 países con más películas
top_countries = df['country'].value_counts().head(20).index
df_top_countries = df[df['country'].isin(top_countries)]

sns.boxplot(x="duration", y="country", data=df_top_countries)
plt.suptitle("Promedio de duración de las películas por País de Origen (Top 20 países)", fontweight="bold")
fig = plt.gcf()
fig.set_size_inches(12, 6)

plt.savefig("Graficas_pract_3/GBigote_Duracion_Pais.png", bbox_inches="tight")
plt.gcf().clear()


#Gráfica de pastel, cantidad de películas por género
df_genres = df['listed_in'].value_counts()
#Calcularé el porcentaje de cada género
genre_percentage = df_genres / df_genres.sum() * 100

#Después filtraré los géneros que tienen más del 5% y los agruparé en "Otros"
df_genres_filtered = genre_percentage[genre_percentage >= 5]
df_genres_other = genre_percentage[genre_percentage < 5].sum()

#Crearé un nuevo dataframe con los géneros filtrados y "Otros"
df_genres_filtered['Other'] = df_genres_other

desfase = [0.1 if x < 5 else 0 for x in df_genres_filtered.values]
df_genres_filtered.plot.pie(autopct="%1.0f%%", startangle=90, figsize=(10, 10), 
                            wedgeprops={'edgecolor': 'black'}, labeldistance=1.1)
plt.suptitle("Cantidad de Películas por Género", fontweight="bold")
plt.axis('equal')  
plt.ylabel('')  

plt.savefig("Graficas_pract_3/GPastel_Generos_Cantidad_Peliculas.png")
plt.gcf().clear()


#Gráfica de Barras, cantidad de películas por año de lanzamiento
df_year = df['release_year'].value_counts().sort_index()
df_year.plot(kind="bar", figsize=(12, 6), color="skyblue")
plt.suptitle("Cantidad de Películas por Año de Lanzamiento", fontweight="bold")
plt.xlabel("Año de Lanzamiento")
plt.ylabel("Cantidad de Películas")
plt.savefig("Graficas_pract_3/GBarras_Peliculas_Año.png")
plt.gcf().clear()

#Gráfica de barras (extra), cantidad de películas por década
#Crearé una nueva columna para agrupar los años por décadas
df['decade'] = (df['release_year'] // 10) * 10
#Contaré la cantidad de películas por década
df_decade = df['decade'].value_counts().sort_index()

df_decade.plot(kind="bar", figsize=(12, 6), color="skyblue", edgecolor="black")
plt.suptitle("Cantidad de Películas por Década", fontweight="bold")
plt.xlabel("Década de Lanzamiento")
plt.ylabel("Cantidad de Películas")

plt.savefig("Graficas_pract_3/GBarras_Peliculas_Decada.png")
plt.gcf().clear()


#Gráfica de Histograma, promedio de duración de las películas
sns.histplot(df['duration'], bins=20, kde=True, color="green")
plt.suptitle("Promedio de Duración de Películas", fontweight="bold")
plt.xlabel("Duración (minutos)")
plt.ylabel("Cantidad de películas")
fig = plt.gcf()
fig.set_size_inches(12, 6)
plt.savefig("Graficas_pract_3/GHistograma_Duracion.png")
plt.gcf().clear()


#Gráfica de Pastel, cantidad de películas por continentes
continents_mapping = {
    'Norteamérica': ['United States', 'Canada', 'Mexico'],
    'Latinoamérica': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Peru', 'Uruguay', 
                      'Venezuela', 'Guatemala', 'Costa Rica', 'Panama', 
                      'Honduras', 'El Salvador', 'Nicaragua'],
    'Europa': ['France', 'Germany', 'United Kingdom', 'Italy', 'Spain', 'Sweden', 'Russia'],
    'África': ['Nigeria', 'South Africa', 'Egypt', 'Morocco', 'Kenya'],
    'Asia': ['India', 'China', 'Japan', 'South Korea', 'Thailand', 'Indonesia'],
    'Oceanía': ['Australia', 'New Zealand']
}

#Agrupación de películas por continente
df['continent'] = df['country'].map(
    lambda country: next((continent for continent, countries in continents_mapping.items() if country in countries), None)
)
df_continents = df['continent'].value_counts()

df_continents.plot.pie(
    autopct="%1.0f%%", startangle=90, figsize=(10, 10), 
    wedgeprops={'edgecolor': 'black'}, labeldistance=1.1
)
plt.suptitle("Cantidad de Películas por Continente", fontweight="bold")
plt.axis('equal')
plt.ylabel(' ')
plt.savefig("Graficas_pract_3/GPastel_Continentes.png")
plt.gcf().clear()

#Gráfica de pastel (extra), cantidad por Top 15 países con más películas
df_countries = df['country'].value_counts()
top_countries = df_countries.head(15)
others_count = df_countries.iloc[15:].sum()

#Crearé un nuevo dataframe con el resto de países que serán agrupados en "Otros" 
top_countries['Otros'] = others_count

top_countries.plot.pie(
    autopct="%1.0f%%", startangle=90, figsize=(10, 10), 
    wedgeprops={'edgecolor': 'black'}, labeldistance=1.1
)
plt.suptitle("Cantidad de Películas por País (Top 15)", fontweight="bold")
plt.axis('equal')
plt.ylabel(' ')
plt.savefig("Graficas_pract_3/GPastel_Paises_Top15_Otros.png")
plt.gcf().clear()