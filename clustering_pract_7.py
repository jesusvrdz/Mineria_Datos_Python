import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import os


df = pd.read_csv('movies_clean.csv')

def Kmeans_release_year_duration():
    top = df.query('movie_id <= 1000')
    top_P = top[["release_year", "duration"]].dropna()

    SumaDistancias = []

    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, random_state=0, n_init=5)
        kmeans.fit_predict(top_P)
        SumaDistancias.append(kmeans.inertia_)
        plt.scatter(x=top_P["release_year"], y=top_P["duration"], c=kmeans.labels_, s=5, cmap='viridis')
        plt.xlabel("Año de Estreno")
        plt.ylabel("Duración (minutos)")
        plt.title(f"Kmeans con K={k}")
        plt.savefig(os.path.join('Grafica_pract_8/Release_Country','Kmeans con K={k}.png'))
        plt.clf()
        
    #Graficaré la suma de cuadrados de distancias en función de n_clusters
    plt.plot(range(1, 10), SumaDistancias, 'bx-')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Suma de Cuadrados de Distancias')
    plt.title('Método del Codo para Determinar k')
    plt.savefig(os.path.join('Grafica_pract_8/Release_Country', 'Metodo del codo de Kmeans.png'))
    plt.show()


def Kmeans_release_year_country():
    top = df.query('movie_id <= 2000')
    top_P = top[["release_year", "country"]].dropna()
    top_P['country_code'] = top_P['country'].astype('category').cat.codes

    SumaDistancias = []

    for k in range(1, 10):
        kmeans = KMeans(n_clusters=k, random_state=0, n_init=5)
        kmeans.fit_predict(top_P[["release_year", "country_code"]])
        SumaDistancias.append(kmeans.inertia_)
        plt.scatter(x=top_P["release_year"], y=top_P["country_code"], c=kmeans.labels_, s=5, cmap='viridis')
        plt.xlabel("Año de Estreno")
        plt.ylabel("Código del País")
        plt.title(f"Kmeans con K={k}")
        plt.savefig(os.path.join('Grafica_pract_8/Release_Country','Kmeans con K={k}.png'))
        plt.clf()
        
    #Graficaré la suma de cuadrados de distancias en función de n_clusters
    plt.plot(range(1, 10), SumaDistancias, 'bx-')
    plt.xlabel('Número de Clusters (k)')
    plt.ylabel('Suma de Cuadrados de Distancias')
    plt.title('Método del Codo para Determinar k')
    plt.savefig(os.path.join('Grafica_pract_8/Release_Country', 'Metodo del codo de Kmeans.png'))
    plt.show()

Kmeans_release_year_duration()
Kmeans_release_year_country()
