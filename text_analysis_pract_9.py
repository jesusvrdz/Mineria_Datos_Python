from wordcloud import WordCloud
import csv
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords


def lectura():
    datos = ""
    stop_words = set(stopwords.words('english')) 
    
    with open('movies_clean.csv', encoding='utf8') as f:
        reader = csv.reader(f)
        next(reader)  
        for row in reader:
            if len(row) > 0:
                texto = row[2]  
                texto = texto.lower()
                palabras = texto.split()
                palabras_filtradas = [palabra for palabra in palabras if palabra not in stop_words]
                datos += " ".join(palabras_filtradas) + " " 
    return datos


def crear_nube_palabras():
    texto = lectura()  
    wordCloud = WordCloud(width=800, height=400, background_color='white').generate(texto)

    plt.imshow(wordCloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    wordCloud.to_file('Word_cloud_pract_9/nube_palabras.png')

crear_nube_palabras()
