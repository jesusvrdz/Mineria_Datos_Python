import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import pandas as pd


df = pd.read_csv("movies_clean.csv")

def Forecasting(category_value, category_column, value_column, title):
    cond1 = df[category_column].str.contains(category_value, na=False)  
    cond2 = df["release_year"] > 1940  
    cond3 = df["release_year"] < 2023  
    df_filtered = df[cond1 & cond2 & cond3]
    df_grouped = df_filtered.groupby("release_year").agg({value_column: "mean"}).reset_index()

    model = smf.ols(f"{value_column} ~ release_year", df_grouped)
    results = model.fit()
    predictions = results.get_prediction(df_grouped).summary_frame(alpha=0.05)

    plt.scatter(df_grouped["release_year"], df_grouped[value_column], s=10, label="Datos reales")
    plt.plot(df_grouped["release_year"], predictions['mean'], color='green', label="Predicción")
    plt.fill_between(
        df_grouped["release_year"],
        predictions['obs_ci_lower'],
        predictions['obs_ci_upper'],
        alpha=0.1,
        color='green',
        label="Intervalo de confianza"
    )
    plt.xlabel("Año de lanzamiento")
    plt.ylabel(value_column)
    plt.title(f"Forecasting: {title}")
    plt.legend()
    plt.savefig(f"Graficas_pract_8/{title}.png")
    plt.close()

Forecasting("Action", "listed_in", "duration", "Action_Duration")
Forecasting("Comedy", "listed_in", "duration", "Comedy_Duration")
Forecasting("Drama", "listed_in", "duration", "Drama_Duration")

