import pandas as pd


dataframe1 = pd.read_excel('facturas.xlsx')

fecha = dataframe1["Fecha"]
abonos = dataframe1["Abonos"]

