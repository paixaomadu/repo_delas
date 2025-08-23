# Criação do Banco
CREATE DATABASE NARA;
USE NARA; 

# Criação das Tabelas ___________________________________________________

#Médico
CREATE TABLE medico(
Id_Medico INT PRIMARY KEY,
Nome VARCHAR(100),
Especialidade VARCHAR(100)
);

#Avaliações
CREATE TABLE avaliacoes(
Id_Consulta INT PRIMARY KEY,
Nota_Satisfacao INT,
Comentario VARCHAR(100)
);

#Pacientes
CREATE TABLE pacientes(
Id_Paciente INT PRIMARY KEY,
Idade VARCHAR(3),
Sexo VARCHAR(1),
Cidade VARCHAR (100),
Plano_Saude VARCHAR(3)
);

#Clinicas
CREATE TABLE clinicas(
Id_Clinica INT PRIMARY KEY,
Nome VARCHAR(50),
Cidade VARCHAR (100),
Capacidade_Diaria INT
);

#Consultas
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

# Permitindo que carregue dados locais na máquina
SET GLOBAL local_infile = 1; 

# Inserção de dados nas tabelas_______________________________________________________

#Médico
LOAD DATA INFILE 'C:/Users/36134552025.1/Documents/Ester/medicos_final.csv'
REPLACE INTO TABLE medico
FIELDS TERMINATED BY ';'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

#Avaliações
LOAD DATA INFILE 'C:/Users/36134552025.1/Documents/Ester/avaliacoes_final.csv'
REPLACE INTO TABLE avaliacoes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; 

#Pacientes
LOAD DATA INFILE 'C:/Users/36134552025.1/Documents/Ester/pacientes_final.csv'
REPLACE INTO TABLE pacientes
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#Clinicas
LOAD DATA INFILE 'C:/Users/36134552025.1/Documents/Ester/clinicas_final.csv'
REPLACE INTO TABLE clinicas
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

#Consultas
LOAD DATA INFILE 'C:/Users/36134552025.1/Documents/Ester/consultas_final.csv'
REPLACE INTO TABLE consultas
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

# Exercícios propostos________________________________________________________

#Total de consultas por especialidade
SELECT Especialidade, COUNT(Especialidade) AS Qnt FROM consultas
WHERE Status_Consulta = 'Realizada'
GROUP BY Especialidade;

#Total de consultas por medico 
SELECT medico.Nome, COUNT(consultas.Id_Medico) AS Qnt FROM consultas
INNER JOIN medico ON medico.Id_Medico = consultas.Id_Medico
WHERE consultas.Status_Consulta = 'Realizada'
GROUP BY medico.Nome
ORDER BY Qnt DESC;

#Total de consultas por consultas 
SELECT clinicas.Nome, COUNT(consultas.Id_Medico) AS Qnt FROM consultas
INNER JOIN clinicas ON clinicas.Id_Clinica = consultas.Id_Clinica
WHERE consultas.Status_Consulta = 'Realizada'
GROUP BY clinicas.Nome
ORDER BY Qnt DESC;

#Total de pacientes por plano de saude
SELECT Plano_Saude, COUNT(Plano_Saude) AS Qnt FROM pacientes
GROUP BY Plano_Saude;

#Total de consultas por status
SELECT Status_Consulta, COUNT(Status_Consulta) AS Qnt FROM consultas
GROUP BY Status_Consulta;





