import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


datos = pd.read_csv('movies_clean.csv')

def RL_DuracionLanzamiento():
    #Tomaré una muestra aleatoria de un 10% de los datos para que sea más visible la gráfica
    datos_muestra = datos.sample(frac=0.1, random_state=42)
    
    sns.lmplot(x='release_year', y='duration', data=datos_muestra, line_kws={'color': 'red'}, scatter_kws={'alpha': 0.5})
    plt.xlabel('Año de Lanzamiento')
    plt.ylabel('Duración (minutos)')
    plt.title('Regresión Lineal: Duración vs Año de Lanzamiento (Muestra Aleatoria)')
    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    
    plt.savefig("Graficas_pract_5/GDispersion_Duracion_Lanzamiento.png")
    plt.close()


def RL_DuracionGenero():
    datos_dramas = datos[datos['listed_in'] == 'Dramas']
    
    #Graficaré la relación entre duración y año de lanzamiento para 'Dramas'
    sns.lmplot(x='release_year', y='duration', data=datos_dramas, line_kws={'color': 'red'}, scatter_kws={'alpha': 0.5})
    plt.xlabel('Año de Lanzamiento')
    plt.ylabel('Duración (minutos)')
    plt.title('Regresión Lineal: Duración vs Año de Lanzamiento (Género: Dramas)')
    fig = plt.gcf()
    fig.set_size_inches(10, 10)
    
    plt.savefig("Graficas_pract_5/GDispersion_Duracion_Lanzamiento_Dramas.png")
    plt.close()

#RL_DuracionLanzamiento()
RL_DuracionGenero()
