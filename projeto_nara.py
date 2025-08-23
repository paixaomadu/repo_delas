#Importação das bibliotecas __________________________________________________________________________________________________
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  imoportação das bases via link do google drive ___________________________________________________________________________
file_id_med = '1tu0E4Xqt7FeprldGQYI4uypcncIOwDHl' 
url_med = f'https://drive.google.com/uc?export=download&id={file_id_med}'

file_id_paci = '1d-ZZjoFHCRym5tGei5cE05974uzPIuQT' 
url_paci = f'https://drive.google.com/uc?export=download&id={file_id_paci}'

file_id_cli = '14w0KYUbEJicByKS7M3upVvWzXKLH8kzQ' 
url_cli = f'https://drive.google.com/uc?export=download&id={file_id_cli}'

file_id_consul = '12bPlpo8oiaEOIuwQni1lKzc6fWKm7QfI' 
url_consul = f'https://drive.google.com/uc?export=download&id={file_id_consul}'

file_id_avali = '1X5cWJUBa712NGzpR5THEU1T4xlEozfoh' 
url_avali = f'https://drive.google.com/uc?export=download&id={file_id_avali}'


#importando todas as bases _________________________________________________________________________________________________
df_med = pd.read_csv (url_med,sep=';', encoding='utf-8')
df_paci = pd.read_csv (url_paci,sep=',', encoding='utf-8')
df_cli = pd.read_csv (url_cli,sep=',', encoding='utf-8')
df_consul = pd.read_csv (url_consul,sep=',', encoding='utf-8')
df_avali = pd.read_csv (url_avali,sep=',', encoding='utf-8')

# Filtra somente as consultas realizadas ___________________________________________________________________________________
df_realizadas= df_consul.loc[df_consul['status'] == 'Realizada']

# Converte para datetime ___________________________________________________________________________________________________
df_realizadas["data_hora_agendada"] = pd.to_datetime(df_realizadas["data_hora_agendada"], errors="coerce", dayfirst=True)  
df_realizadas["data_hora_inicio"] = pd.to_datetime(df_realizadas["data_hora_inicio"], errors="coerce", dayfirst=True) 

# Criar uma coluna para tempo de espera e fazer o calculo da espera em minuto _______________________________________________
df_realizadas['tempo_espera_min'] = ((df_realizadas['data_hora_inicio'] - df_realizadas['data_hora_agendada']).dt.total_seconds() / 60)

# Média e mediana por especialidade  _______________________________________________________________________________________

# Cardiologia 
# Filtra somente cardiologia
df_cardio= df_realizadas.loc[df_consul['especialidade'] == 'Cardiologia']

#array
array_cardio= df_cardio['tempo_espera_min']
dados_cardio= np.array(array_cardio)

#média, mediana e distância
media_cardio= np.mean(dados_cardio)
media_cardio

mediana_cardio= np.median(dados_cardio)
mediana_cardio

distancia_cardio= (media_cardio - mediana_cardio) / mediana_cardio *100
distancia_cardio

#quartil
q1_cardio= np.percentile(dados_cardio, 25)
q2_cardio= np.percentile(dados_cardio, 50)
q3_cardio= np.percentile(dados_cardio, 75)

#Intervalo de interquartil
IQR= q3_cardio - q1_cardio

#limite superior e inferior
ls_cardio= q3_cardio + (1.5 * IQR)
li_cardio= q1_cardio - (1.5 * IQR)

# Dermatologia 
# Filtra somente dermatologia
df_dermatologia= df_realizadas.loc[df_consul['especialidade'] == 'Dermatologia']

#array
array_dermatologia= df_dermatologia['tempo_espera_min']
dados_dermatologia= np.array(array_dermatologia)

#média, mediana e distância
media_dermatologia= np.mean(dados_dermatologia)
media_dermatologia

mediana_dermatologia= np.median(dados_dermatologia)
mediana_dermatologia

distancia_dermatologia= (media_dermatologia - mediana_dermatologia) / mediana_dermatologia *100
distancia_dermatologia

#quartil
q1_dermatologia= np.percentile(dados_dermatologia, 25)
q2_dermatologia= np.percentile(dados_dermatologia, 50)
q3_dermatologia= np.percentile(dados_dermatologia, 75)

#Intervalo de interquartil
IQR= q3_dermatologia - q1_dermatologia

#limite superior e inferior
ls_dermatologia= q3_dermatologia + (1.5 * IQR)
li_dermatologia= q1_dermatologia - (1.5 * IQR)

# Ginecologia 
# Filtra somente ginecologia
df_ginecologia= df_realizadas.loc[df_consul['especialidade'] == 'Ginecologia']

#array
array_ginecologia= df_ginecologia['tempo_espera_min']
dados_ginecologia= np.array(array_ginecologia)

#média, mediana e distância
media_ginecologia= np.mean(dados_ginecologia)
media_ginecologia

mediana_ginecologia= np.median(dados_ginecologia)
mediana_ginecologia

distancia_ginecologia= (media_ginecologia - mediana_ginecologia) / mediana_ginecologia *100
distancia_ginecologia

#quartil
q1_ginecologia= np.percentile(dados_ginecologia, 25)
q2_ginecologia= np.percentile(dados_ginecologia, 50)
q3_ginecologia= np.percentile(dados_ginecologia, 75)

#Intervalo de interquartil
IQR= q3_ginecologia - q1_ginecologia

#limite superior e inferior
ls_ginecologia= q3_ginecologia + (1.5 * IQR)
li_ginecologia= q1_ginecologia - (1.5 * IQR)

# Neurologia 
# Filtra somente neurologia
df_neurologia= df_realizadas.loc[df_consul['especialidade'] == 'Neurologia']

#array
array_neurologia= df_neurologia['tempo_espera_min']
dados_neurologia= np.array(array_neurologia)

#média, mediana e distância
media_neurologia= np.mean(dados_neurologia)
media_neurologia

mediana_neurologia= np.median(dados_neurologia)
mediana_neurologia

distancia_neurologia= (media_neurologia - mediana_neurologia) / mediana_neurologia *100
distancia_neurologia

#quartil
q1_neurologia= np.percentile(dados_neurologia, 25)
q2_neurologia= np.percentile(dados_neurologia, 50)
q3_neurologia= np.percentile(dados_neurologia, 75)

#Intervalo de interquartil
IQR= q3_neurologia - q1_neurologia

#limite superior e inferior
ls_neurologia= q3_neurologia + (1.5 * IQR)
li_neurologia= q1_neurologia - (1.5 * IQR)

# Ortopedia 
# Filtra somente ortopedia
df_ortopedia= df_realizadas.loc[df_consul['especialidade'] == 'Ortopedia']

#array
array_ortopedia= df_ortopedia['tempo_espera_min']
dados_ortopedia= np.array(array_ortopedia)

#média, mediana e distância
media_ortopedia= np.mean(dados_ortopedia)
media_ortopedia

mediana_ortopedia= np.median(dados_ortopedia)
mediana_ortopedia

distancia_ortopedia= (media_ortopedia - mediana_ortopedia) / mediana_ortopedia *100
distancia_ortopedia

#quartil
q1_ortopedia= np.percentile(dados_ortopedia, 25)
q2_ortopedia= np.percentile(dados_ortopedia, 50)
q3_ortopedia= np.percentile(dados_ortopedia, 75)

#Intervalo de interquartil
IQR= q3_ortopedia - q1_ortopedia

#limite superior e inferior
ls_ortopedia= q3_ortopedia + (1.5 * IQR)
li_ortopedia= q1_ortopedia - (1.5 * IQR)


# Pediatria 
# Filtra somente pediatria
df_pediatria= df_realizadas.loc[df_consul['especialidade'] == 'Pediatria']

#array
array_pediatria= df_pediatria['tempo_espera_min']
dados_pediatria= np.array(array_pediatria)

#média, mediana e distância
media_pediatria= np.mean(dados_pediatria)
media_pediatria

mediana_pediatria= np.median(dados_pediatria)
mediana_pediatria

distancia_pediatria= (media_pediatria - mediana_pediatria) / mediana_pediatria *100
distancia_pediatria

#quartil
q1_pediatria= np.percentile(dados_pediatria, 25)
q2_pediatria= np.percentile(dados_pediatria, 50)
q3_pediatria= np.percentile(dados_pediatria, 75)

#Intervalo de interquartil
IQR= q3_pediatria - q1_pediatria

#limite superior e inferior
ls_pediatria= q3_pediatria + (1.5 * IQR)
li_pediatria= q1_pediatria - (1.5 * IQR)

# Média e mediana por medico  _______________________________________________________________________________________

df_med = df_realizadas.groupby('id_medico')['tempo_espera_min'].mean().reset_index()
df_med = df_realizadas.groupby('id_medico')['tempo_espera_min'].median().reset_index()


df_medico_comp=pd.merge(clientes, pedidos, left_on='id', right_on='cliente_id',
how='inner')
















medicos = df_med['nome'].unique()
dados_medicos = []
dfs_por_medico = {}

for id_med in medicos:
    df_medico = df_med[df_med['nome'] == id_med]
    
    if df_medico.empty:
        continue
    
    dfs_por_medico[id_med] = df_medico  # Armazena o df completo daquele médico
    
    #array
    array_pediatria= df_pediatria['tempo_medio_atendimento']
    dados_pediatria= np.array(array_pediatria)

    #média, mediana e distância
    media_pediatria= np.mean(dados_pediatria)
    media_pediatria

    mediana_pediatria= np.median(dados_pediatria)
    mediana_pediatria

    distancia_pediatria= (media_pediatria - mediana_pediatria) / mediana_pediatria *100
    distancia_pediatria

    #quartil
    q1_pediatria= np.percentile(dados_pediatria, 25)
    q2_pediatria= np.percentile(dados_pediatria, 50)
    q3_pediatria= np.percentile(dados_pediatria, 75)

    #Intervalo de interquartil
    IQR= q3_pediatria - q1_pediatria

    #limite superior e inferior
    ls_pediatria= q3_pediatria + (1.5 * IQR)
    li_pediatria= q1_pediatria - (1.5 * IQR)

