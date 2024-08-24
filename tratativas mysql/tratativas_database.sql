-- Distribuição de vendas por país, região e categoria de produto
SELECT 
    l.Pais AS Pais,
    l.Cidade AS Cidade,
    p.Categoria_Produto AS Categoria,
    ROUND(SUM(v.Quantidade * v.Preco_Unitario), 2) AS Total_Vendas
FROM 
    Vendas v
JOIN 
    Lojas l ON v.ID_Loja = l.ID_Loja
JOIN 
    Produtos p ON v.ID_Produto = p.ID_Produto
GROUP BY 
    l.Pais, l.Cidade, p.Categoria_Produto
ORDER BY 
    Total_Vendas DESC;

-- Tendências de vendas ao longo do tempo
SELECT 
    YEAR(v.Data_Venda) AS Ano,
    MONTH(v.Data_Venda) AS Mes,
    ROUND(SUM(v.Quantidade * v.Preco_Unitario), 2) AS Total_Vendas
FROM 
    Vendas v
GROUP BY 
    YEAR(v.Data_Venda), MONTH(v.Data_Venda)
ORDER BY 
    Ano, Mes;

-- Produtos mais vendidos e menos vendidos
-- Produtos mais vendidos
SELECT 
    p.Nome_Produto AS Produto,
    SUM(v.Quantidade) AS Quantidade_Vendida,
    ROUND(SUM(v.Quantidade * v.Preco_Unitario), 2) AS Valor_Total_Vendido
FROM 
    Vendas v
JOIN 
    Produtos p ON v.ID_Produto = p.ID_Produto
GROUP BY 
    p.Nome_Produto
ORDER BY 
    Quantidade_Vendida DESC
LIMIT 10;

-- Produtos menos vendidos
SELECT 
    p.Nome_Produto AS Produto,
    SUM(v.Quantidade) AS Quantidade_Vendida,
    ROUND(SUM(v.Quantidade * v.Preco_Unitario), 2) AS Valor_Total_Vendido
FROM 
    Vendas v
JOIN 
    Produtos p ON v.ID_Produto = p.ID_Produto
GROUP BY 
    p.Nome_Produto
ORDER BY 
    Quantidade_Vendida ASC
LIMIT 10;

-- Clientes mais valiosos e sua distribuição geográfica
SELECT 
    c.ID_Cliente AS Cliente_ID,
    c.Satisfacao_Cliente AS Satisfacao,
    l.Pais AS Pais,
    l.Cidade AS Cidade,
    ROUND(SUM(v.Quantidade * v.Preco_Unitario), 2) AS Total_Gasto
FROM 
    Vendas v
JOIN 
    Clientes c ON v.ID_Cliente = c.ID_Cliente
JOIN 
    Lojas l ON v.ID_Loja = l.ID_Loja
GROUP BY 
    c.ID_Cliente, c.Satisfacao_Cliente, l.Pais, l.Cidade
ORDER BY 
    Total_Gasto DESC
LIMIT 10;

SELECT 
    p.Nome_Produto, 
    p.Categoria_Produto,
    vendas.Total_Vendido AS Total_Produtos_Vendidos,
    categorias.Total_Vendido AS Total_Categoria_Vendida,
    ROUND(lucro.Lucro_Total, 2) AS Lucro_Total
FROM 
    Produtos p
JOIN 
    (
        -- Subconsulta para o ranking de produtos mais vendidos
        SELECT 
            v.ID_Produto, 
            SUM(v.Quantidade) AS Total_Vendido
        FROM 
            Vendas v
        GROUP BY 
            v.ID_Produto
    ) AS vendas ON p.ID_Produto = vendas.ID_Produto
JOIN 
    (
        -- Subconsulta para categorias mais populares
        SELECT 
            p.Categoria_Produto, 
            SUM(v.Quantidade) AS Total_Vendido
        FROM 
            Vendas v
        JOIN 
            Produtos p ON v.ID_Produto = p.ID_Produto
        GROUP BY 
            p.Categoria_Produto
    ) AS categorias ON p.Categoria_Produto = categorias.Categoria_Produto
JOIN 
    (
        -- Subconsulta para análise de lucratividade
        SELECT 
            v.ID_Produto, 
            SUM((v.Preco_Unitario - p.Preco_Base) * v.Quantidade) AS Lucro_Total
        FROM 
            Vendas v
        JOIN 
            Produtos p ON v.ID_Produto = p.ID_Produto
        GROUP BY 
            v.ID_Produto
    ) AS lucro ON p.ID_Produto = lucro.ID_Produto
ORDER BY 
    Total_Produtos_Vendidos DESC;

WITH Ranking_Produtos AS (
    SELECT 
        p.ID_Produto, 
        p.Nome_Produto, 
        p.Categoria_Produto,
        SUM(v.Quantidade) AS Total_Vendido
    FROM 
        Vendas v
    JOIN 
        Produtos p ON v.ID_Produto = p.ID_Produto
    GROUP BY 
        p.ID_Produto, p.Nome_Produto, p.Categoria_Produto
),
Categorias_Populares AS (
    SELECT 
        p.Categoria_Produto, 
        SUM(v.Quantidade) AS Total_Vendido_Categoria
    FROM 
        Vendas v
    JOIN 
        Produtos p ON v.ID_Produto = p.ID_Produto
    GROUP BY 
        p.Categoria_Produto
),
Analise_Lucratividade AS (
    SELECT 
        v.ID_Produto,
        SUM((v.Preco_Unitario - p.Preco_Base) * v.Quantidade) AS Lucro_Total
    FROM 
        Vendas v
    JOIN 
        Produtos p ON v.ID_Produto = p.ID_Produto
    GROUP BY 
        v.ID_Produto
),
Alertas_Preco_Base AS (
    SELECT 
        p.ID_Produto, 
        p.Nome_Produto, 
        v.Preco_Unitario, 
        p.Preco_Base,
        (p.Preco_Base - v.Preco_Unitario) AS Diferença
    FROM 
        Vendas v
    JOIN 
        Produtos p ON v.ID_Produto = p.ID_Produto
    WHERE 
        v.Preco_Unitario < p.Preco_Base
    GROUP BY 
        p.ID_Produto, p.Nome_Produto, v.Preco_Unitario, p.Preco_Base
)

SELECT 
    rp.Nome_Produto, 
    rp.Categoria_Produto,
    rp.Total_Vendido AS Total_Produtos_Vendidos,
    cp.Total_Vendido_Categoria AS Total_Categoria_Vendida,
    ROUND(al.Lucro_Total, 2) AS Lucro_Total,
    CASE
        WHEN ap.ID_Produto IS NOT NULL THEN 'Alerta: Preço Base Muito Maior'
        ELSE 'OK'
    END AS Status_Alerta
FROM 
    Ranking_Produtos rp
JOIN 
    Categorias_Populares cp ON rp.Categoria_Produto = cp.Categoria_Produto
LEFT JOIN 
    Analise_Lucratividade al ON rp.ID_Produto = al.ID_Produto
LEFT JOIN 
    Alertas_Preco_Base ap ON rp.ID_Produto = ap.ID_Produto
GROUP BY
    rp.Nome_Produto, rp.Categoria_Produto, rp.Total_Vendido, cp.Total_Vendido_Categoria, al.Lucro_Total, ap.ID_Produto
ORDER BY 
    rp.Total_Vendido DESC;

USE seu_banco_de_dados;  -- Substitua 'seu_banco_de_dados' pelo nome do seu banco de dados

WITH Segmentacao_Clientes AS (
    SELECT 
        c.ID_Cliente,
        CASE 
            WHEN c.Satisfacao_Cliente >= 4 THEN 'Alta'
            WHEN c.Satisfacao_Cliente BETWEEN 2 AND 3 THEN 'Média'
            ELSE 'Baixa'
        END AS Segmento_Satisfacao,
        COUNT(v.ID_Venda) AS Total_Compras
    FROM 
        Clientes c
    LEFT JOIN 
        Vendas v ON c.ID_Cliente = v.ID_Cliente
    GROUP BY 
        c.ID_Cliente, c.Satisfacao_Cliente
),
Analise_Cohort AS (
    SELECT 
        c.ID_Cliente,
        CONCAT(c.Ano_Inicio_Seguir, '-', LPAD(c.Mes_Inicio_Seguir, 2, '0')) AS Periodo_Inicio,
        COUNT(v.ID_Venda) AS Total_Compras_Cohort
    FROM 
        Clientes c
    LEFT JOIN 
        Vendas v ON c.ID_Cliente = v.ID_Cliente
    GROUP BY 
        c.ID_Cliente, c.Ano_Inicio_Seguir, c.Mes_Inicio_Seguir
),
Valor_Medio_Compra AS (
    SELECT 
        v.ID_Cliente,
        AVG(v.Preco_Unitario) AS Valor_Medio_Compra
    FROM 
        Vendas v
    GROUP BY 
        v.ID_Cliente
)

SELECT 
    sc.ID_Cliente,
    sc.Segmento_Satisfacao,
    sc.Total_Compras,
    ac.Periodo_Inicio,
    ac.Total_Compras_Cohort,
    ROUND(vmc.Valor_Medio_Compra, 2) AS Valor_Medio_Compra
FROM 
    Segmentacao_Clientes sc
LEFT JOIN 
    Analise_Cohort ac ON sc.ID_Cliente = ac.ID_Cliente
LEFT JOIN 
    Valor_Medio_Compra vmc ON sc.ID_Cliente = vmc.ID_Cliente
GROUP BY 
    sc.ID_Cliente, sc.Segmento_Satisfacao, sc.Total_Compras, ac.Periodo_Inicio, ac.Total_Compras_Cohort, vmc.Valor_Medio_Compra
ORDER BY 
    sc.Total_Compras DESC, vmc.Valor_Medio_Compra DESC;
