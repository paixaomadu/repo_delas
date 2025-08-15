import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Opção de link via google drive

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


#importando todas as bases
df_medico = pd.read_csv (url_medico,sep=';', encoding='ISO-8859-1')
df_pacientes = pd.read_csv (url_pacientes,sep=';', encoding='ISO-8859-1')
df_clinicas = pd.read_csv (url_clinicas,sep=';', encoding='ISO-8859-1')
df_consultas = pd.read_csv (url_consultas,sep=';', encoding='ISO-8859-1')
df_avaliacoes = pd.read_csv (url_avaliacoes,sep=';', encoding='ISO-8859-1')


# Criando uma lista pra facilitar o concat
lista_dfs = [df_medico,df_pacientes,df_clinicas,df_consultas,df_avaliacoes]

# Juntando as bases 
df= pd.concat(lista_dfs, ignore_index=True)








