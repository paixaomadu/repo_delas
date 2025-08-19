#Importação das bibliotecas -------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  imoportação das bases via link do google drive

file_id_med = '1_oEoWVme6mKfqhl2Itlkb53u_EFz_u8s' 
url_med = f'https://drive.google.com/uc?export=download&id={file_id_med}'

file_id_paci = '1d-ZZjoFHCRym5tGei5cE05974uzPIuQT' 
url_paci = f'https://drive.google.com/uc?export=download&id={file_id_paci}'

file_id_cli = '14w0KYUbEJicByKS7M3upVvWzXKLH8kzQ' 
url_cli = f'https://drive.google.com/uc?export=download&id={file_id_cli}'

file_id_consul = '12bPlpo8oiaEOIuwQni1lKzc6fWKm7QfI' 
url_consul = f'https://drive.google.com/uc?export=download&id={file_id_consul}'

file_id_avali = '1X5cWJUBa712NGzpR5THEU1T4xlEozfoh' 
url_avali = f'https://drive.google.com/uc?export=download&id={file_id_avali}'


#importando todas as bases
df_med = pd.read_csv (url_med,sep=',', encoding='utf-8')
df_paci = pd.read_csv (url_paci,sep=',', encoding='utf-8')
df_cli = pd.read_csv (url_cli,sep=',', encoding='utf-8')
df_consul = pd.read_csv (url_consul,sep=',', encoding='utf-8')
df_avali = pd.read_csv (url_avali,sep=',', encoding='utf-8')


# Criando uma lista pra facilitar o concat
lista = [df_med,df_paci,df_cli,df_consul,df_avali]

# Converte para datetime a data agendada
df_consul["data_hora_agendada"] = pd.to_datetime(df_consul["data_hora_agendada"], errors="coerce", dayfirst=True)  # ajusta dayfirst conforme seu formato

# Separa data e hora
df_consul['data_agendada'] = df_consul['data_hora_agendada'].dt.date   # Apenas a data
df_consul['hora_agendada'] = df_consul['data_hora_agendada'].dt.time    # Apenas a hora

# Converte para datetime a data de inicio
df_consul["data_hora_inicio"] = pd.to_datetime(df_consul["data_hora_inicio"], errors="coerce", dayfirst=True)  # ajusta dayfirst conforme seu formato

# Separa data e hora
df_consul['data_inicio'] = df_consul['data_hora_inicio'].dt.date   # Apenas a data
df_consul['hora_inicio'] = df_consul['data_hora_inicio'].dt.time    # Apenas a hora

