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

# 📦 Passo a Passo para Utilização do Cassandra via Docker

## Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop) instalado em sua máquina.

## 🚀 Instruções

1. **Baixe e instale o Docker Desktop**  
   👉 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

2. **Abra o terminal e execute o seguinte comando para iniciar o container do Cassandra**:

   ```bash
     docker run --name cassandra-container -d -p 9042:9042 cassandra:latest
   ```

3. **Verifique se a imagem foi baixada corretamente**:

   ```bash
   docker images
   ```

4. **Acesse o shell interativo do Cassandra (CQLSH)**:

   ```bash
   docker exec -it cassandra_db cqlsh
   ```

5. **Caso queira parar o Cassandra**, utilize:

   ```bash
   exit
   ```
   
# 🐬 MySQL com Docker + Workbench

## 🎥 Vídeo de apoio  
Caso esqueça algum passo, veja o vídeo:  
[📺 Tutorial MySQL no Docker + Workbench](https://youtu.be/a5ul8o76Hqw?si=DICC2MKbN59JIyoN)

---

## 🛠️ Instalar o MySQL Workbench

Baixe o instalador oficial:  
🔗 [https://dev.mysql.com/downloads/windows/installer/8.0.html](https://dev.mysql.com/downloads/windows/installer/8.0.html)

Durante a instalação:

- Selecione a opção **Custom**
- Instale a **versão mais atual** de:
  - **MySQL Server**
  - **MySQL Workbench**
  - **MySQL Examples and Samples**
- Defina uma **senha segura** para o usuário `root`

---

## 🐳 Inicializar o MySQL no Docker

### Fazer linha por linha

Usar o docker-compose-mysql.yml para poder rodar e dps executa-lo
```bash
docker exec -it mysql-db mysql -u root -p
```

## 📦 Inicializar o MONGODB no Docker

### Fazer linha por linha

Usar o docker-compose-mongodb.yml para poder rodar e dps executa-lo
```bash
docker exec -it mongodb mongosh -u root -p root
```
