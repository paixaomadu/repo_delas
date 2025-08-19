import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1 - Opção de link via google drive

file_id_medico = '1_oEoWVme6mKfqhl2Itlkb53u_EFz_u8s' 
url_medico = f'https://drive.google.com/uc?export=download&id={file_id_medico}'

file_id_pacientes = '1d-ZZjoFHCRym5tGei5cE05974uzPIuQT' 
url_pacientes = f'https://drive.google.com/uc?export=download&id={file_id_pacientes}'

file_id_clinicas = '14w0KYUbEJicByKS7M3upVvWzXKLH8kzQ' 
url_clinicas = f'https://drive.google.com/uc?export=download&id={file_id_clinicas}'

file_id_consultas = '12bPlpo8oiaEOIuwQni1lKzc6fWKm7QfI' 
url_consultas = f'https://drive.google.com/uc?export=download&id={file_id_consultas}'

file_id_avaliacoes = '1X5cWJUBa712NGzpR5THEU1T4xlEozfoh' 
url_avaliacoes = f'https://drive.google.com/uc?export=download&id={file_id_avaliacoes}'


# 2 - importando todas as bases
df_medico = pd.read_csv (url_medico,sep=',', encoding='utf-8')
df_pacientes = pd.read_csv (url_pacientes,sep=',', encoding='utf-8')
df_clinicas = pd.read_csv (url_clinicas,sep=',', encoding='utf-8')
df_consultas = pd.read_csv (url_consultas,sep=',', encoding='utf-8')
df_avaliacoes = pd.read_csv (url_avaliacoes,sep=',', encoding='utf-8')


# 3- Criando uma lista pra facilitar o concat
lista_dfs = [df_medico,df_pacientes,df_clinicas,df_consultas,df_avaliacoes]

# 4 - Transformando as colunas de data no tipo data

df_consultas['data_hora_agendada'] = pd.to_datetime(df_consultas['data_hora_agendada'], errors= "coerce", dayfirst=True)
df_consultas['data_hora_inicio'] = pd.to_datetime(df_consultas['data_hora_inicio'], errors= "coerce", dayfirst=True)

# 5 - Cálculo de tempo de espera consultas realizadas_______________________________________________________________________________________________________________

# 5.1 - Filtrando apenas as consultas realizadas 
df_consultas_espera = df_consultas.loc[df_consultas['status'] == 'Realizada'].copy()

# 5.2 - Calculando tempo de espera em minutos
df_consultas_espera['Tempo_de_espera(min)'] = ((df_consultas_espera['data_hora_inicio'] - df_consultas_espera['data_hora_agendada']).dt.total_seconds() / 60)


# 6 - Cálculo de tempo de espera consultas realizadas_______________________________________________________________________________________________________________

# 6.1 - Filtrando apenas as consultas realizadas 
df_consultas_canceladas= df_consultas.loc[df_consultas['status'] == 'Cancelada'].copy()

# 6.2 - Calculando tempo de espera em minutos
df_consultas_canceladas['Tempo_de_espera(min)'] = ((df_consultas_canceladas['data_hora_inicio'] - df_consultas_canceladas['data_hora_agendada']).dt.total_seconds() / 60)


# ___________________________________________________Média e mediana por Especialidade_______________________________________________________________________________

# CARDIOLOGIA -----------------------------------------------------------------------------------------
df_cardio = df_consultas_espera.loc[df_consultas_espera['especialidade']== 'Cardiologia']

# transformando em array
dados_cardio= np.array(df_cardio['Tempo_de_espera(min)'])

#Calculo de medidas de tendencias centrais 
media_cardio = np.mean(df_cardio['Tempo_de_espera(min)'])
mediana_cardio = np.median(df_cardio['Tempo_de_espera(min)'])
distancia_cardio = ((media_cardio - mediana_cardio)/mediana_cardio) *100

#quartis
cardio_q1= np.percentile(dados_cardio,25)
cardio_q2= np.percentile(dados_cardio,50)
cardio_q3= np.percentile(dados_cardio,75)

cardio_iqr= cardio_q3 - cardio_q1
cardio_ls= cardio_q3 + (1.5*cardio_iqr) #limite superior
cardio_li= cardio_q1 - (1.5*cardio_iqr) # limite inferior

cardio_outliers = df_cardio[(df_cardio['Tempo_de_espera(min)'] < cardio_li) | (df_cardio['Tempo_de_espera(min)'] > cardio_ls)]

# Exibição dos resultados
print(f'Média: {media_cardio:.2f}\nMediana: {mediana_cardio:.2f}\nDistância: {distancia_cardio:.2f}%')

##### fazer Desvio padrão 


# DERMATOLOGIA   -----------------------------------------------------------------------------------------
df_dermato = df_consultas_espera.loc[df_consultas_espera['especialidade']== 'Dermatologia']

# transformando em array
dados_dermato= np.array(df_dermato['Tempo_de_espera(min)'])

#Calculo de medidas de tendencias centrais 
media_dermato = np.mean(df_dermato['Tempo_de_espera(min)'])
mediana_dermato = np.median(df_dermato['Tempo_de_espera(min)'])
distancia_dermato = ((media_dermato - mediana_dermato)/mediana_dermato) *100

#quartis
dermato_q1= np.percentile(dados_dermato,25)
dermato_q2= np.percentile(dados_dermato,50)
dermato_q3= np.percentile(dados_dermato,75)

dermato_iqr= dermato_q3 - dermato_q1
dermato_ls= dermato_q3 + (1.5*dermato_iqr) #limite superior
dermato_li= dermato_q1 - (1.5*dermato_iqr) # limite inferior

dermato_outliers = df_dermato[(df_dermato['Tempo_de_espera(min)'] < dermato_li) | (df_dermato['Tempo_de_espera(min)'] > dermato_ls)]

# Exibição dos resultados
print(f'Média: {media_dermato:.2f}\nMediana: {mediana_dermato:.2f}\nDistância: {distancia_dermato:.2f}%')


# GINECOLOGIA --------------------------------------------------------------------------------------------

df_gineco = df_consultas_espera.loc[df_consultas_espera['especialidade']== 'Ginecologia']

# transformando em array
dados_gineco= np.array(df_gineco['Tempo_de_espera(min)'])

#Calculo de medidas de tendencias centrais 
media_gineco = np.mean(df_gineco['Tempo_de_espera(min)'])
mediana_gineco = np.median(df_gineco['Tempo_de_espera(min)'])
distancia_gineco = ((media_gineco - mediana_gineco)/mediana_gineco) *100

#quartis
gineco_q1= np.percentile(dados_gineco,25)
gineco_q2= np.percentile(dados_gineco,50)
gineco_q3= np.percentile(dados_gineco,75)

gineco_iqr= gineco_q3 - gineco_q1
gineco_ls= gineco_q3 + (1.5*gineco_iqr) #limite superior
gineco_li= gineco_q1 - (1.5*gineco_iqr) # limite inferior

gineco_outliers = df_gineco[(df_gineco['Tempo_de_espera(min)'] < gineco_li) | (df_gineco['Tempo_de_espera(min)'] > gineco_ls)]

# Exibição dos resultados
print(f'Média: {media_gineco:.2f}\nMediana: {mediana_gineco:.2f}\nDistância: {distancia_gineco:.2f}%')

# NEUROLOGIA ---------------------------------------------------------------------------------------------

df_neuro = df_consultas_espera.loc[df_consultas_espera['especialidade']== 'Neurologia']

# transformando em array
dados_neuro= np.array(df_neuro['Tempo_de_espera(min)'])

#Calculo de medidas de tendencias centrais 
media_neuro = np.mean(df_neuro['Tempo_de_espera(min)'])
mediana_neuro = np.median(df_neuro['Tempo_de_espera(min)'])
distancia_neuro = ((media_neuro - mediana_neuro)/mediana_neuro) *100

#quartis
neuro_q1= np.percentile(dados_neuro,25)
neuro_q2= np.percentile(dados_neuro,50)
neuro_q3= np.percentile(dados_neuro,75)

neuro_iqr= neuro_q3 - neuro_q1
neuro_ls= neuro_q3 + (1.5*neuro_iqr) #limite superior
neuro_li= neuro_q1 - (1.5*neuro_iqr) # limite inferior

neuro_outliers = df_neuro[(df_neuro['Tempo_de_espera(min)'] < neuro_li) | (df_neuro['Tempo_de_espera(min)'] > neuro_ls)]

# Exibição dos resultados
print(f'Média: {media_neuro:.2f}\nMediana: {mediana_neuro:.2f}\nDistância: {distancia_neuro:.2f}%')


# ORTOPEDIA -----------------------------------------------------------------------------------------

df_ortoped = df_consultas_espera.loc[df_consultas_espera['especialidade']== 'Ortopedia']

# transformando em array
dados_ortoped= np.array(df_ortoped['Tempo_de_espera(min)'])

#Calculo de medidas de tendencias centrais 
media_ortoped = np.mean(df_ortoped['Tempo_de_espera(min)'])
mediana_ortoped = np.median(df_ortoped['Tempo_de_espera(min)'])
distancia_ortoped = ((media_ortoped - mediana_ortoped)/mediana_ortoped) *100

#quartis
ortoped_q1= np.percentile(dados_ortoped,25)
ortoped_q2= np.percentile(dados_ortoped,50)
ortoped_q3= np.percentile(dados_ortoped,75)

ortoped_iqr= ortoped_q3 - ortoped_q1
ortoped_ls= ortoped_q3 + (1.5*ortoped_iqr) #limite superior
ortoped_li= ortoped_q1 - (1.5*ortoped_iqr) # limite inferior

ortoped_outliers = df_ortoped[(df_ortoped['Tempo_de_espera(min)'] < ortoped_li) | (df_ortoped['Tempo_de_espera(min)'] > ortoped_ls)]

# Exibição dos resultados
print(f'Média: {media_ortoped:.2f}\nMediana: {mediana_ortoped:.2f}\nDistância: {distancia_ortoped:.2f}%')


# PEDIATRIA -----------------------------------------------------------------------------------------

df_pedi = df_consultas_espera.loc[df_consultas_espera['especialidade']== 'Pediatria']

# transformando em array
dados_pedi= np.array(df_pedi['Tempo_de_espera(min)'])

#Calculo de medidas de tendencias centrais 
media_pedi = np.mean(df_pedi['Tempo_de_espera(min)'])
mediana_pedi = np.median(df_pedi['Tempo_de_espera(min)'])
distancia_pedi = ((media_pedi - mediana_pedi)/mediana_pedi) *100

#quartis
pedi_q1= np.percentile(dados_pedi,25)
pedi_q2= np.percentile(dados_pedi,50)
pedi_q3= np.percentile(dados_pedi,75)

pedi_iqr= pedi_q3 - pedi_q1
pedi_ls= pedi_q3 + (1.5*pedi_iqr) #limite superior
pedi_li= pedi_q1 - (1.5*pedi_iqr) # limite inferior

pedi_outliers = df_pedi[(df_pedi['Tempo_de_espera(min)'] < pedi_li) | (df_pedi['Tempo_de_espera(min)'] > pedi_ls)]

# Exibição dos resultados
print(f'Média: {media_pedi:.2f}\nMediana: {mediana_pedi:.2f}\nDistância: {distancia_pedi:.2f}%')


### fazer isso tudo pra medico e clinica #vaitomarnouc

