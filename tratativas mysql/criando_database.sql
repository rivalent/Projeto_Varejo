-- Selecione o banco de dados
USE projeto_varejoGH;

-- Verifique o diretório seguro para arquivos
SHOW VARIABLES LIKE 'secure_file_priv';

-- Crie a tabela redessociais
DROP TABLE IF EXISTS redessociais;
CREATE TABLE redessociais (
    ID_Engajamento INT,
    ID_Cliente INT,
    Data_Engajamento DATE,
    Tipo_Engajamento VARCHAR(100),
    Rede_Social VARCHAR(100)
);

-- Carregue os dados na tabela redessociais
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/engajamento_redes_sociais.csv'
INTO TABLE redessociais
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Engajamento, ID_Cliente, Data_Engajamento, Tipo_Engajamento, Rede_Social);

-- Crie a tabela campanhasmarketing
DROP TABLE IF EXISTS campanhasmarketing;
CREATE TABLE campanhasmarketing (
    ID_Campanha INT,
    Nome_Campanha VARCHAR(100),
    Canal_Divulgacao VARCHAR(100),
    Publico_Alvo VARCHAR(100),
    Data_Inicio DATETIME,
    Data_Fim DATETIME
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/campanhas_marketing.csv'
INTO TABLE campanhasmarketing
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Campanha, Nome_Campanha, Canal_Divulgacao, Publico_Alvo, Data_Inicio, Data_Fim);

DROP TABLE IF EXISTS clientes;
CREATE TABLE clientes (
    ID_Cliente INT,
    Satisfacao_Cliente INT,
    Mes_Inicio_Seguir INT,
    Ano_Inicio_Seguir YEAR
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/clientes.csv'
INTO TABLE clientes
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Cliente,Satisfacao_Cliente,Mes_Inicio_Seguir,Ano_Inicio_Seguir);

DROP TABLE IF EXISTS lojas;
CREATE TABLE lojas (
    ID_Loja INT,
    Nome_Loja VARCHAR(100),
    Cidade VARCHAR(100),
    Pais VARCHAR(100)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/lojas_corrigidas.csv'
INTO TABLE lojas
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Loja,Nome_Loja,Cidade,Pais);

DROP TABLE IF EXISTS produtos;
CREATE TABLE produtos (
    ID_Produto INT,
    Categoria_Produto VARCHAR(100),
    Preco_Base FLOAT,
    Nome_Produto VARCHAR(100)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/produtos_corrigidos.csv'
INTO TABLE produtos
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Produto,Categoria_Produto,Preco_Base,Nome_Produto);

DROP TABLE IF EXISTS promocoes;
CREATE TABLE promocoes (
    ID_Promocao INT,
    Data_Inicio DATETIME,
    Data_Fim DATETIME,
    Desconto FLOAT,
    ID_Produto INT
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/promocoes.csv'
INTO TABLE promocoes
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Promocao,Data_Inicio,Data_Fim,Desconto,ID_Produto);

DROP TABLE IF EXISTS vendas;
CREATE TABLE vendas (
    ID_Venda INT,
    ID_Produto INT,
    ID_Loja INT,
    Data_Venda DATETIME,
    Quantidade INT,
    Preco_Unitario FLOAT,
    ID_Cliente INT,
    Desconto FLOAT,
    Promocao CHAR(1),
    Estoque_Inicial INT,
    Estoque_Final INT,
    Devolucao CHAR(1)
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/vendas_tratadas.csv'
INTO TABLE vendas
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(ID_Venda,ID_Produto,ID_Loja,Data_Venda,Quantidade,Preco_Unitario,ID_Cliente,Desconto,Promocao,Estoque_Inicial,Estoque_Final,Devolucao);
