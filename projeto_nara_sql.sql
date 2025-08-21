CREATE DATABASE nara;
USE nara;

CREATE TABLE medico (
id_medico INT PRIMARY KEY,
nome VARCHAR(200),
especialidade VARCHAR(100),
tempo_medio_atendimento INT
);

ALTER TABLE medico DROP COLUMN tempo_medio_atendimento;

LOAD DATA INFILE 'C:\Users\36134552025.1\Downloads\medicos_final.csv' #fazer com todos os outros
INTO TABLE medico
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 


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

CREATE TABLE avaliacao (
id_cosulta INT PRIMARY KEY,
nota_satisfacao VARCHAR(2),
comentario VARCHAR(100)
);

SET GLOBAL local_infile = 1; 

LOAD DATA INFILE 'C:/Users/36134552025.1/Documents/vendas.csv'
INTO TABLE medico
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 