import pandas as pd


df = pd.read_excel("ddd19_004.xlsx")

nome = input("Digite o nome: ")


resultado = df[df["NOME"].str.contains(nome.upper(), na=False)]

resultado.to_csv("pessoas.csv")


print(resultado)
