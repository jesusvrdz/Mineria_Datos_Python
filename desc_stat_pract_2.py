#Estadística descriptiva
import csv
import pandas as pd


#Análisis para observar la relación de la duración con el género
def EstadisticasPorGeneroYDuracion():
    #Número de géneros únicos
    #total_generos = df['listed_in'].nunique()
    #print(f"Total de géneros únicos: {total_generos}\n")

    #Agrupamos las estadísticas por género
    resultado = df.groupby('listed_in')['duration'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.columns = ['Total_Peliculas', 'Duracion_Promedio', 'Duracion_Minima', 'Duracion_Maxima', 'Desviacion_Estandar', 'Varianza']
    
    #print(resultado)
    resultado.to_csv('Tablas_pract_2/DataSet_Genero_Duracion.csv')


#Análisis para observar la relación de la duración promedio por país
def EstadisticasPorPaisYDuracion():
    #Duración promedio por país
    resultado = df.groupby('country')['duration'].agg(['mean', 'min', 'max', 'std', 'var'])
    resultado.columns = ['Duracion_Promedio', 'Duracion_Minima', 'Duracion_Maxima', 'Desviacion_Estandar', 'Varianza']
    
    #print(resultado) 
    resultado.to_csv('Tablas_pract_2/DataSet_Pais_Duracion.csv')


#Análisis para observar la estadisticas de los directores
def EstadisticasPorDirector():
    #Agrupamos por director y calculamos las estadísticas para la cantidad de películas
    resultado = df.groupby('director')['duration'].agg(['count', 'mean', 'min', 'max', 'std', 'var'])
    resultado.columns = ['Total_Peliculas', 'Duracion_Promedio', 'Duracion_Minima', 'Duracion_Maxima', 'Desviacion_Estandar', 'Varianza']
    
    #print(resultado)
    resultado.to_csv('Tablas_pract_2/DataSet_Director_Peliculas_Duracion.csv')


#Análisis para observar cuantas peliculas se agregan por mes
def EstadisticasPorFechaAgregada():
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    #Extraemos el mes en el que se añadieron las películas
    df['month_added'] = df['date_added'].dt.month
    
    #Agrupamos por mes, contamos las películas y hacemos los cálculos
    resultado = df.groupby('month_added').size().reset_index(name='Total_Peliculas')
    resultado['Promedio_Peliculas'] = resultado['Total_Peliculas'].mean()
    resultado['Peliculas_Minimas'] = resultado['Total_Peliculas'].min()
    resultado['Peliculas_Maximas'] = resultado['Total_Peliculas'].max()
    resultado['Desviacion_Estandar'] = resultado['Total_Peliculas'].std()
    resultado['Varianza'] = resultado['Total_Peliculas'].var()

    #print(resultado)
    resultado.to_csv('Tablas_pract_2/DataSet_Peliculas_Agregadas_Por_Mes.csv')

df = pd.read_csv("movies_clean.csv")

EstadisticasPorGeneroYDuracion()
EstadisticasPorPaisYDuracion()
EstadisticasPorDirector()
EstadisticasPorFechaAgregada()
