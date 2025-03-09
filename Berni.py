import pandas as pd

def charge(archivo):
    extension = archivo.split('.')[-1].lower()

    if extension == 'csv':
        df = pd.read_csv(archivo)
    elif extension == 'xlsx':
        df = pd.read_excel(archivo)
    elif extension == 'json':
        df = pd.read_json(archivo)
    elif extension == 'html':
        df = pd.read_html(archivo)
    else:
        print("Archivo no compatible, intente de nuevo.")

    df.to_csv("nuevo_df.csv", index=False)
    return df

def fusili(df):
    return df.fillna(method='ffill')

def boloñesa(df):
    return df.fillna(method='bfill')

def spaguetti(df, valor="Desconocido"):
    return df.fillna(valor)

def pomodoro(df):
    return df.fillna(df.mean())

def pizza(df):
    return df.fillna(df.median())

def picante(df, valor=0):
    return df.fillna(valor)

def olivos(df):
    nulos_por_columna = df.isnull().sum()
    nulos_totales = df.isnull().sum().sum()
    return nulos_por_columna, nulos_totales