# Fitstore: Sistema para Gestão de Treinos e Nutrição

## 📌 Sobre o Projeto  
Este projeto surgiu a partir do interesse dos integrantes do grupo por academia e bem-estar. O objetivo é desenvolver um sistema completo que auxilie nos treinos, na nutrição e na compra de produtos relacionados, abrangendo todas as necessidades para um desempenho otimizado.  

## 🔥 Funcionalidades  
O sistema será dividido em três principais módulos:  

### 🛒 Loja Virtual  
- Venda de roupas esportivas (camisetas, leggings, tênis, luvas etc.)
- Venda de equipamentos para treino (halteres, colchonetes, faixas elásticas, barras etc.)
- Venda de suplementos (Whey Protein, Creatina, pré-treinos etc.)  

### 🍎 Planejamento Alimentar  
- Base de dados com diversos alimentos, contendo seus valores nutricionais e classificações (ex.: proteína, carboidrato, gordura, etc.)  
- Geração de um plano alimentar personalizado para cada usuário, levando em conta suas metas individuais (ganho de massa, emagrecimento, manutenção, etc.)  
- Ajuste automático das quantidades de cada alimento com base nos objetivos do usuário  

### 🏋️‍♂️ Gestão de Treinos  
- Base de dados com exercícios, contendo informações como: grupo muscular trabalhado, equipamento necessário, nível de dificuldade e instruções de execução  
- Criação de treinos personalizados para cada usuário, adaptando a carga, volume e intensidade conforme a experiência e objetivo (hipertrofia, resistência, força, etc.)  
- Geração de treinos com base nos grupos musculares selecionados e no foco do usuário  

## 🗄️ Tecnologias e Bancos de Dados 
Para a implementação do projeto, serão utilizados três bancos de dados diferentes:  

- **MySQL** (Relacional - RDB)  
- **Cassandra** (NoSQL - DB1)  
- **MongoDB** (NoSQL - DB2)  

A escolha dos bancos de dados foi feita com o propósito de explorar novas tecnologias, pelo menos dois deles são bancos que ainda não foram utilizados pelos integrantes do grupo, permitindo que seja ampliado o conhecimento e experiência na área.  


## O que será armazenado no Cassandra (DB1):

-> Gestão de Treinos
- Históricos de treino dos usuários
- Séries e execuções por data
- Consultas rápidas por usuário e período
- Dados densos e com acesso massivo (ex.: treinos do dia)

-------------------------------
CODIGO CASSANDRA

CREATE KEYSPACE fitstore
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE fitstore;

CREATE TABLE treinos_usuario (
    id_usuario UUID,
    data DATE,
    id_treino UUID,
    grupo_muscular TEXT,
    exercicio TEXT,
    series INT,
    repeticoes INT,
    carga INT,
    PRIMARY KEY ((id_usuario), data, id_treino)
) WITH CLUSTERING ORDER BY (data DESC);

-------------------------------
