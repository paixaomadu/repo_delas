import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1 - Opção de link via google drive

file_id_medico = '1tu0E4Xqt7FeprldGQYI4uypcncIOwDHl' 
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
df_medico = pd.read_csv (url_medico,sep=';', encoding='utf-8')
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

# 6.3 - Transformando em Float pra facilitar futuros calculos
df_consultas_espera['Tempo_de_espera(min)'] = df_consultas_espera['Tempo_de_espera(min)'].astype('Float64')

#exportando pra csv
df_consultas_espera.to_csv('evolucao_bolsa.csv', index=False)

# ___________________________________________________Média e mediana por Especialidade_______________________________________________________________________________

# CARDIOLOGIA -----------------------------------------------------------------------------------------
df_cardio = df_consultas_espera.loc[df_consultas_espera['especialidade']== 'Cardiologia']

# transformando em array
dados_cardio= np.array(df_cardio['Tempo_de_espera(min)'])

#Calculo de medidas de tendencias centrais 
media_cardio = np.mean(df_cardio['Tempo_de_espera(min)'])
mediana_cardio = np.median(df_cardio['Tempo_de_espera(min)'])
distancia_cardio = ((media_cardio - mediana_cardio)/mediana_cardio) *100
desvio_padrao_cardio = np.std(df_cardio['Tempo_de_espera(min)'], ddof=1)

#quartis
cardio_q1= np.percentile(dados_cardio,25)
cardio_q2= np.percentile(dados_cardio,50)
cardio_q3= np.percentile(dados_cardio,75)

# feito pelo desvio padrão 
cardio_iqr= cardio_q3 - cardio_q1
cardio_ls= media_cardio + 2*desvio_padrao_cardio #limite superior
cardio_li= media_cardio - 2*desvio_padrao_cardio # limite inferior


cardio_outliers = df_cardio[(df_cardio['Tempo_de_espera(min)'] < cardio_li) | (df_cardio['Tempo_de_espera(min)'] > cardio_ls)]

# Exibição dos resultados
print(f'Média: {media_cardio:.2f}\nMediana: {mediana_cardio:.2f}\nDistância: {distancia_cardio:.2f}%')




# DERMATOLOGIA   -----------------------------------------------------------------------------------------
df_dermato = df_consultas_espera.loc[df_consultas_espera['especialidade']== 'Dermatologia']

# transformando em array
dados_dermato= np.array(df_dermato['Tempo_de_espera(min)'])

#Calculo de medidas de tendencias centrais 
media_dermato = np.mean(df_dermato['Tempo_de_espera(min)'])
mediana_dermato = np.median(df_dermato['Tempo_de_espera(min)'])
distancia_dermato = ((media_dermato - mediana_dermato)/mediana_dermato) *100
desvio_padrao_dermato = np.std(df_dermato['Tempo_de_espera(min)'], ddof=1)

#quartis
dermato_q1= np.percentile(dados_dermato,25)
dermato_q2= np.percentile(dados_dermato,50)
dermato_q3= np.percentile(dados_dermato,75)

# feito pela formula normal com mudança na regra do iqr
dermato_iqr= dermato_q3 - dermato_q1
dermato_ls= dermato_q3 + (0.5*dermato_iqr) #limite superior
dermato_li= dermato_q1 - (0.5*dermato_iqr) # limite inferior

# feito pelo desvio padrão 
dermato_ls_dp= media_dermato + 2*desvio_padrao_dermato #limite superior
dermato_li_dp= media_dermato - 2*desvio_padrao_dermato # limite inferior

dermato_outliers = df_dermato[(df_dermato['Tempo_de_espera(min)'] < dermato_li) | (df_dermato['Tempo_de_espera(min)'] > dermato_ls)]
dermato_outliers_dp = df_dermato[(df_dermato['Tempo_de_espera(min)'] < dermato_li_dp) | (df_dermato['Tempo_de_espera(min)'] > dermato_ls_dp)]

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
desvio_padrao_gineco = np.std(df_gineco['Tempo_de_espera(min)'], ddof=1)

#quartis
gineco_q1= np.percentile(dados_gineco,25)
gineco_q2= np.percentile(dados_gineco,50)
gineco_q3= np.percentile(dados_gineco,75)

# feito pela formula normal com mudança na regra do iqr
gineco_iqr= gineco_q3 - gineco_q1
gineco_ls= gineco_q3 + (0.5*gineco_iqr) #limite superior
gineco_li= gineco_q1 - (0.5*gineco_iqr) # limite inferior

# feito pelo desvio padrão 
gineco_ls_dp= media_gineco + 2*desvio_padrao_gineco #limite superior
gineco_li_dp= media_gineco - 2*desvio_padrao_gineco # limite inferior

gineco_outliers = df_gineco[(df_gineco['Tempo_de_espera(min)'] < gineco_li) | (df_gineco['Tempo_de_espera(min)'] > gineco_ls)]
gineco_outliers_dp = df_gineco[(df_gineco['Tempo_de_espera(min)'] < gineco_li_dp) | (df_gineco['Tempo_de_espera(min)'] > gineco_ls_dp)]

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
desvio_padrao_neuro = np.std(df_neuro['Tempo_de_espera(min)'], ddof=1)

#quartis
neuro_q1= np.percentile(dados_neuro,25)
neuro_q2= np.percentile(dados_neuro,50)
neuro_q3= np.percentile(dados_neuro,75)

# feito pela formula normal com mudança na regra do iqr
neuro_iqr= neuro_q3 - neuro_q1
neuro_ls= neuro_q3 + (0.5*neuro_iqr) #limite superior
neuro_li= neuro_q1 - (0.5*neuro_iqr) # limite inferior

# feito pelo desvio padrão 
neuro_ls_dp= media_neuro + 2*desvio_padrao_neuro #limite superior
neuro_li_dp= media_neuro - 2*desvio_padrao_neuro # limite inferior

neuro_outliers = df_neuro[(df_neuro['Tempo_de_espera(min)'] < neuro_li) | (df_neuro['Tempo_de_espera(min)'] > neuro_ls)]
neuro_outliers_dp = df_neuro[(df_neuro['Tempo_de_espera(min)'] < neuro_li_dp) | (df_neuro['Tempo_de_espera(min)'] > neuro_ls_dp)]

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
desvio_padrao_ortoped = np.std(df_ortoped['Tempo_de_espera(min)'], ddof=1)

#quartis
ortoped_q1= np.percentile(dados_ortoped,25)
ortoped_q2= np.percentile(dados_ortoped,50)
ortoped_q3= np.percentile(dados_ortoped,75)

# feito pela formula normal com mudança na regra do iqr
ortoped_iqr= ortoped_q3 - ortoped_q1
ortoped_ls= ortoped_q3 + (0.5*ortoped_iqr) #limite superior
ortoped_li= ortoped_q1 - (0.5*ortoped_iqr) # limite inferior

# feito pelo desvio padrão 
ortoped_ls_dp= media_ortoped + 2*desvio_padrao_ortoped #limite superior
ortoped_li_dp= media_ortoped - 2*desvio_padrao_ortoped # limite inferior

ortoped_outliers = df_ortoped[(df_ortoped['Tempo_de_espera(min)'] < ortoped_li) | (df_ortoped['Tempo_de_espera(min)'] > ortoped_ls)]
ortoped_outliers_dp = df_ortoped[(df_ortoped['Tempo_de_espera(min)'] < ortoped_li_dp) | (df_ortoped['Tempo_de_espera(min)'] > ortoped_ls_dp)]

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
desvio_padrao_pedi = np.std(df_pedi['Tempo_de_espera(min)'], ddof=1)

#quartis
pedi_q1= np.percentile(dados_pedi,25)
pedi_q2= np.percentile(dados_pedi,50)
pedi_q3= np.percentile(dados_pedi,75)

# feito pela formula normal com mudança na regra do iqr
pedi_iqr= pedi_q3 - pedi_q1
pedi_ls= pedi_q3 + (0.5*pedi_iqr) #limite superior
pedi_li= pedi_q1 - (0.5*pedi_iqr) # limite inferior

# feito pelo desvio padrão 
pedi_ls_dp= media_pedi + 2*desvio_padrao_pedi #limite superior
pedi_li_dp= media_pedi - 2*desvio_padrao_pedi # limite inferior

pedi_outliers = df_pedi[(df_pedi['Tempo_de_espera(min)'] < pedi_li) | (df_pedi['Tempo_de_espera(min)'] > pedi_ls)]
pedi_outliers_dp = df_pedi[(df_pedi['Tempo_de_espera(min)'] < pedi_li_dp) | (df_pedi['Tempo_de_espera(min)'] > pedi_ls_dp)]


# Exibição dos resultados
print(f'Média: {media_pedi:.2f}\nMediana: {mediana_pedi:.2f}\nDistância: {distancia_pedi:.2f}%')

# ___________________________________________________Média e mediana por Médico_______________________________________________________________________________

# Pd merge para juntar o df de medico e de tempo
df_medico_merge = pd.merge(df_medico, df_consultas_espera, on='id_medico', how='inner')

# Média, mediana e distância
df_med_media = df_medico_merge.groupby('nome')['Tempo_de_espera(min)'].mean().round(1).reset_index()
df_med_mediana= df_medico_merge.groupby('nome')['Tempo_de_espera(min)'].median().reset_index()

# Adicionando uma coluna "distancia" atravez do calculo feito com a media e mediana 
df_distancia = pd.merge(df_med_media, df_med_mediana, on='nome', suffixes=('_media', '_mediana')) #suffixer: adicionando um sufixo nas colunas novas
df_distancia['distancia'] = (df_distancia['Tempo_de_espera(min)_media'] - df_distancia['Tempo_de_espera(min)_mediana']).abs().round(2) #abs para trazer valor absoluto

# Função para mostrar os dados do médico através de uma busca ***********************************

def buscar_medico(nome):
    resultado = df_distancia.loc[df_distancia['nome'] == nome ]
    print(resultado)

# buscar_medico("Dr(a). Ricardo Souza") - medico usado como exemplo

# Função que busca os outliers por medico********************************************************

def buscar_outliers_medico(nome):
    # Filtra os dados do médico
    df_filtro_unitario = df_medico_merge.loc[df_medico_merge['nome'] == nome]

    if df_filtro_unitario.empty:
        print(f"Médico '{nome}' não encontrado.")
        return
    else: 
        print(f"Médico '{nome}' encontrado.")

    # criando o array
    dados_med= np.array(df_filtro_unitario['Tempo_de_espera(min)'])

    # Calcula Q1, Q3 e IQR
    q1 = np.percentile(dados_med, 25)
    q3 = np.percentile(dados_med,75)
    iqr = q3 - q1

    limite_inferior = q1 - (1.5 * iqr)
    limite_superior = q3 + (1.5 * iqr)

    # Filtra as linhas que são outliers
    outliers = df_filtro_unitario[(df_filtro_unitario['Tempo_de_espera(min)'] < limite_inferior) |(df_filtro_unitario['Tempo_de_espera(min)'] > limite_superior)]

    # Retorna os resultados
    if outliers.empty:
        print(f"Nenhum outlier encontrado para o médico '{nome}'.")
    else:
        print(f"Outliers encontrados para o médico '{nome}':")
        print(outliers.to_string(index=False))

# buscar_outliers_medico("Dr(a). Ricardo Souza") - medico de exmplo para a consulta


# ___________________________________________________Média e mediana por Clínica_______________________________________________________________________________
        
# Pd merge para juntar o df de clinica e de tempo
df_clinica_merge = pd.merge(df_clinicas, df_consultas_espera, on='id_clinica', how='inner')

# Média, mediana e distância

df_clinica_media = df_clinica_merge.groupby('nome')['Tempo_de_espera(min)'].mean().round(1).reset_index()
df_clinica_mediana= df_clinica_merge.groupby('nome')['Tempo_de_espera(min)'].median().reset_index()

# Junta média e mediana em um df para criar uma tabela com media, mediana e distancia

df_distancia_clinica= pd.merge(df_clinica_media, df_clinica_mediana, on='nome', suffixes=('_media', '_mediana')) #suffixer para renomear as colunas
df_distancia_clinica['distancia'] = (df_distancia_clinica['Tempo_de_espera(min)_media'] - df_distancia_clinica['Tempo_de_espera(min)_mediana']).abs().round(2) #abs para trazer valor absoluto

# Função para mostrar os dados da clinica
def buscar_clinica(nome):
    resultado = df_distancia_clinica.loc[df_distancia_clinica['nome'] == nome ]
    print(resultado)



#Função para mostrar os outliers da clinica
def buscar_outliers_clinica(nome):

    # Filtra os dados da clinica
    df_filtro_unitario = df_clinica_merge[df_clinica_merge['nome'] == nome]

    if df_filtro_unitario.empty:
        print(f"Médico '{nome}' não encontrado.")
        return
    
    # criando o array
    dados_clinica= np.array(df_filtro_unitario['Tempo_de_espera(min)'])

    # Q1, Q3 e IQR
    q1 = np.percentile(dados_clinica,25) 
    q3 = np.percentile(dados_clinica,75)
    iqr = q3 - q1

    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr

    # Filtra as linhas que são outliers
    outliers = df_filtro_unitario[(df_filtro_unitario['Tempo_de_espera(min)'] < limite_inferior) |(df_filtro_unitario['Tempo_de_espera(min)'] > limite_superior)]

    # resultado
    if outliers.empty:
        print(f"Nenhum outlier encontrado para a clinica '{nome}'.")
    else:
        print(f"Outliers encontrados para a clinica '{nome}':")
        print(outliers.to_string(index=False))




#correlacao entre tempo de espera e satisfacao
df_tempo_espera = df_consultas_espera.groupby('id_consulta')['Tempo_de_espera(min)'].sum().reset_index()
df_tempo_espera = df_consultas_espera.sort_values(by='Tempo_de_espera(min)', ascending= False)
df_nota_satisfacao = df_avaliacoes.groupby('id_consulta')['nota_satisfacao'].sum().reset_index()
df_nota_satisfacao = df_nota_satisfacao.sort_values(by='nota_satisfacao', ascending= True)


#fazer um pd merge inner 
tempo_espera_satisfacao = pd.merge(df_tempo_espera, df_nota_satisfacao, on = 'id_consulta', how= 'inner')


#pegar o tamanho do df avaliacoes e o tamanho do df tempo de espera satisfacao e tirar uma porcentagem
#fazer a funcao para outlier de medico e clinica