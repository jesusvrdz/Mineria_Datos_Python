import pandas as pd
from scipy.stats import f_oneway, ttest_ind, kruskal
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('movies_clean.csv')

#------------------------------ ANOVA Forma - 1 ------------------------------------------------------------#
#Comprobación
def comprobar_anova(df_aux: pd.DataFrame, formula: str):
    modelo = ols(formula, data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modelo, typ=2)
    if anova_df["PR(>F)"][0] < 0.05:
        print("Hay diferencias significativas entre los grupos.")
        print(anova_df)
    else:
        print("No hay diferencias significativas entre los grupos.")

#------------------------------ Asignar Décadas ------------------------------------------------------------#
#Asignamos la década a cada película
def asignar_decada(df):
    df['decade'] = (df['release_year'] // 10) * 10
    return df

df = asignar_decada(df)

#------------------------------ Limitar Décadas y Géneros ---------------------------------------------#
#Limitaré las décadas y géneros para una mejor visualización
def filtrar_datos(df):
    df = df[df['decade'].isin([1960, 1980, 2010])]
    df = df[df['listed_in'].isin(['Dramas', 'Comedies'])]
    return df

df = filtrar_datos(df)

#Comparamos la duración promedio por década y género
def anova_1():
    #Agrupamos por década y género para obtener la duración promedio
    df_by_type = df.groupby(["decade", "listed_in"]).agg({"duration": "mean"})
    df_by_type.reset_index(inplace=True)
    comprobar_anova(df_by_type, "duration ~ decade + listed_in")
    
#------------------------------ Visualización con Boxplot ------------------------------------------------------------#
    #Gráfica de bigotes para comparar la duración por década y género
    plt.figure(figsize=(14, 8))  # Tamaño de la figura ajustado
    sns.boxplot(x="decade", y="duration", hue="listed_in", data=df, palette="Set2")
    
    plt.title("Comparación de la duración de películas por década y género (ANOVA 1)", fontsize=16)
    plt.xlabel("Década", fontsize=14)
    plt.ylabel("Duración (minutos)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(title="Género", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)
    plt.tight_layout()
    plt.show()


#------------------------------ ANOVA Forma - 2 ------------------------------------------------------------#
#Comprobación
def comprobar_anova(df_aux: pd.DataFrame, formula: str):
    modelo = ols(formula, data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modelo, typ=2)
    if anova_df["PR(>F)"][0] < 0.05:
        print("Hay diferencias significativas entre los grupos.")
        print(anova_df)
    else:
        print("No hay diferencias significativas entre los grupos.")

#------------------------------ Asignar Décadas ------------------------------------------------------------#
#Asignamos la década a cada película
def asignar_decada(df):
    df['decade'] = (df['release_year'] // 10) * 10
    return df

df = asignar_decada(df)

#------------------------------ Limitar Países y Géneros ---------------------------------------------#
#Limitaremos los países y géneros para fines prácticos
def filtrar_datos(df):
    df = df[df['country'].isin(['United States', 'India', 'Mexico', 'Canada', 'United Kingdom'])]
    df = df[df['listed_in'].isin(['Dramas', 'Comedies'])]
    return df

df = filtrar_datos(df)

#------------------------------ ANOVA por País y Género --------------------------------------------#
def anova_2():
    #Agrupamos por país y género para obtener la duración promedio
    df_by_type = df.groupby(["country", "listed_in"]).agg({"duration": "mean"})
    df_by_type.reset_index(inplace=True)
    comprobar_anova(df_by_type, "duration ~ country + listed_in")
    
#------------------------------ Visualización con Boxplot ------------------------------------------------------------#
    #Gráfica de bigote para comparar la duración por país y género
    plt.figure(figsize=(14, 8))  
    sns.boxplot(x="country", y="duration", hue="listed_in", data=df, palette="Set2")
    plt.title("Comparación de la duración de películas por país y género (ANOVA 2)", fontsize=16)
    plt.xlabel("País", fontsize=14)
    plt.ylabel("Duración (minutos)", fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(title="Género", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)
    plt.tight_layout()
    plt.show()


#------------------------------ T-test comparación entre géneros en década de 1980 ----------------------------#
def t_test():
    df_80s = df[df['decade'] == 1980]  
    dramas = df_80s[df_80s['listed_in'] == 'Dramas']['duration']
    comedies = df_80s[df_80s['listed_in'] == 'Comedies']['duration']
    t_stat, p_val = ttest_ind(dramas, comedies)
    
    print(f"T-statistic: {t_stat}, P-value: {p_val}")
    if p_val < 0.05:
        print("Hay diferencias significativas entre los géneros en los 80s.")
    else:
        print("No hay diferencias significativas entre los géneros en los 80s.")

#------------------------------ Visualización con Boxplot ----------------------------#
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='listed_in', y='duration', data=df_80s, palette='Set2')
    plt.title("Comparación de duración entre Géneros (Década de 1980), T Test", fontsize=16)
    plt.xlabel("Género", fontsize=14)
    plt.ylabel("Duración (minutos)", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()


#------------------------------ Kruskal-Wallis Test comparación entre países ----------------------------#
def kruskal_test():
    #Agrupamos las películas por país
    grupo_usa = df[df['country'] == 'United States']['duration']
    grupo_mexico = df[df['country'] == 'Mexico']['duration']
    grupo_india = df[df['country'] == 'India']['duration']
    #Realizamos el Kruskal-Wallis test
    stat, p_val = kruskal(grupo_usa, grupo_mexico, grupo_india)
    
    print(f"Kruskal-Wallis Statistic: {stat}, P-value: {p_val}")
    if p_val < 0.05:
        print("Hay diferencias significativas entre los países.")
    else:
        print("No hay diferencias significativas entre los países.")

#------------------------------ Visualización con Boxplot ----------------------------#
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='country', y='duration', data=df[df['country'].isin(['United States', 'Mexico', 'India'])], palette='Set2')
    plt.title("Comparación de duración por país (Kruskal Wallis Test)", fontsize=16)
    plt.xlabel("País", fontsize=14)
    plt.ylabel("Duración (minutos)", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

#anova_1()   
#anova_2()   
#t_test()  
kruskal_test()  