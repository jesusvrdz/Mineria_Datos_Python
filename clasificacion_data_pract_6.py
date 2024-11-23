import pandas as pd
import matplotlib.pyplot as plt


datos = pd.read_csv('movies_clean.csv')

def Duracion_Fecha():
    Children_Family = datos[datos["listed_in"].str.contains("Children & Family Movies")]
    Documentaries = datos[datos["listed_in"].str.contains("Documentaries")]
    Horror = datos[datos["listed_in"].str.contains("Horror Movies")]
    
    plt.scatter(Children_Family["duration"], Children_Family["release_year"], marker="+", s=30, color="blue", label="Children & Family Movies")

    plt.scatter(Documentaries["duration"], Documentaries["release_year"], marker="x", s=30, color="red", label="Documentaries")

    plt.scatter(Horror["duration"], Horror["release_year"], marker="1", s=30, color="green", label="Horror Movies")
    
    plt.ylabel("Año de Estreno")
    plt.xlabel("Duración de la Película (minutos)")
    plt.title("Duración de Películas por Año de Estreno")
    plt.legend(bbox_to_anchor=(1, 0.2))
    
    plt.savefig("Graficas_pract_6/GDispersion_Duracion_Fecha.png")
    plt.show()

Duracion_Fecha()

