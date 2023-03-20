import pandas as pd

df_2010 = pd.read_csv("2010.csv")
df_2011 = pd.read_csv("2011.csv")
df_2012 = pd.read_csv("2012.csv")
df_2014 = pd.read_csv("2014.csv")
df_2015 = pd.read_csv("2015.csv")
df_2016 = pd.read_csv("2016.csv")
df_2017 = pd.read_csv("2017.csv")
df_2018 = pd.read_csv("2018.csv")
df_2019 = pd.read_csv("2019.csv")
df_2020 = pd.read_csv("2020.csv")



limites_columnas = ["Depreg","Mupreg","Mesreg","Añoreg","Libras","Onzas","Sexo","Tipar","Tohite","Tohim","Tohivi"]

df_2010 = df_2010[limites_columnas]
df_2011 = df_2011[limites_columnas]
df_2012 = df_2012[limites_columnas]
df_2014 = df_2014[limites_columnas]
df_2015 = df_2015[limites_columnas]
df_2016 = df_2016[limites_columnas]
df_2017 = df_2017[limites_columnas]
df_2018 = df_2018[limites_columnas]
df_2019 = df_2019[limites_columnas]
df_2020 = df_2020[limites_columnas]

df_final = pd.concat([df_2010,df_2011,df_2012,df_2014,df_2015,df_2016,df_2017,df_2018,df_2019,df_2020])
df_final.to_csv("data_set_completo.csv",index=False)


