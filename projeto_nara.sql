#Criação do banco de dados
CREATE DATABASE nara;
USE nara;

#Criação de tabela 
CREATE TABLE medico (
id_medico INT PRIMARY KEY,
nome VARCHAR(200),
especialidade VARCHAR(100),
tempo_medio_atendimento INT
);

#Remoção da coluna tempo medio da tabela medico
ALTER TABLE medico DROP COLUMN tempo_medio_atendimento;


CREATE TABLE pacientes (
id_paciente INT PRIMARY KEY,
idade VARCHAR(3),
sexo VARCHAR(1),
cidade VARCHAR(100),
plano_saude VARCHAR(3)
);

CREATE TABLE clinica (
id_clinica INT PRIMARY KEY,
nome VARCHAR(100),
cidade VARCHAR(100),
capacidade_diaria VARCHAR(3)
);

CREATE TABLE consulta (
id_consulta INT PRIMARY KEY,
id_paciente INT, FOREIGN KEY (id_paciente) REFERENCES pacientes(id_paciente),
id_medico INT, FOREIGN KEY (id_medico) REFERENCES medico(id_medico),
id_clinica INT, FOREIGN KEY (id_clinica) REFERENCES clinica(id_clinica),
especialidade VARCHAR(100),
data_hora_agendada DATE,
data_hora_inicio DATE,
status_consul VARCHAR(100)
);

#Mudando o tipo de data 
ALTER TABLE consulta
MODIFY COLUMN data_hora_agendada DATETIME,
MODIFY COLUMN data_hora_inicio DATETIME;

CREATE TABLE avaliacao (
id_cosulta INT PRIMARY KEY,
nota_satisfacao VARCHAR(2),
comentario VARCHAR(100)
);

#Permissão de dados locais
SET GLOBAL local_infile = 1; 

#Adicionando as informações em cada tabela
LOAD DATA INFILE 'C:/Users/36134552025.1/Downloads/medicos_final (1).csv' 
INTO TABLE medico
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

LOAD DATA INFILE 'C:/Users/36134552025.1/Downloads/pacientes_final.csv' 
INTO TABLE pacientes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

LOAD DATA INFILE 'C:/Users/36134552025.1/Downloads/clinicas_final.csv' 
INTO TABLE clinica
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

LOAD DATA INFILE 'C:/Users/36134552025.1/Downloads/consultas_final.csv'
REPLACE INTO TABLE consulta
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

LOAD DATA INFILE 'C:/Users/36134552025.1/Downloads/avaliacoes_final.csv' 
INTO TABLE avaliacao
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

SELECT *FROM pacientes;

#Total de consultas por especialidade
SELECT especialidade, COUNT(especialidade) AS quant FROM consulta
WHERE status_consul = 'Realizada'
GROUP BY especialidade;

#Total de consultas por medico 
SELECT medico.nome, COUNT(consulta.id_medico) AS quant FROM consulta
INNER JOIN medico ON medico.id_medico = consulta.id_medico
WHERE consulta.status_consul = 'Realizada'
GROUP BY medico.nome
ORDER BY quant DESC;

#Total de consultas por clinica
SELECT clinica.nome, COUNT(consulta.id_clinica) AS quant FROM consulta
INNER JOIN clinica ON clinica.id_clinica = consulta.id_clinica
WHERE consulta.status_consul = 'Realizada'
GROUP BY clinica.nome
ORDER BY quant DESC;

#Total de pacientes por plano de saúde
SELECT plano_saude, COUNT(plano_saude) AS quant FROM pacientes
GROUP BY plano_saude;

#Total de consultas por status
SELECT status_consul, COUNT(status_consul) AS quant FROM consulta
GROUP BY status_consul;









