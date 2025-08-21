CREATE DATABASE NARA;
USE NARA; 

CREATE TABLE medico(
Id_Medico INT PRIMARY KEY,
Nome VARCHAR(100),
Especialidade VARCHAR(100)
);

CREATE TABLE avaliacoes(
Id_Consulta INT PRIMARY KEY,
Nota_Satisfacao INT,
Comentario VARCHAR(100)
);

CREATE TABLE pacientes(
Id_Paciente INT PRIMARY KEY,
Idade VARCHAR(3),
Sexo VARCHAR(1),
Cidade VARCHAR (100),
Plano_Saude VARCHAR(3)
);

CREATE TABLE clinicas(
Id_Clinica INT PRIMARY KEY,
Nome VARCHAR(50),
Cidade VARCHAR (100),
Capacidade_Diaria INT
);

CREATE TABLE consultas(
Id_Consulta INT PRIMARY KEY,
Id_Paciente INT, FOREIGN KEY (Id_Paciente) REFERENCES pacientes(Id_Paciente),
Id_Medico INT, FOREIGN KEY (Id_Medico) REFERENCES medico(Id_Medico),
Id_Clinica INT, FOREIGN KEY (Id_Clinica) REFERENCES clinicas(Id_Clinica),
Especialidade VARCHAR (50),
Data_Hora_Agendada DATETIME,
Data_Hora_Inicio DATETIME,
Status_Consulta VARCHAR (15)
);

SET GLOBAL local_infile = 1; 

''' LOAD DATA INFILE 'C:/Users/36134552025.1/Documents/vendas.csv'
INTO TABLE Vendas_novas
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; '''









