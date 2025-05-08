# FitHouse: Sistema para Gestão de Treinos e Nutrição
FitHouse é um aplicativo focado na gestão de treinos e planejamento alimentar, criado para ajudar usuários a alcançarem seus objetivos de saúde, desempenho e bem-estar. O sistema combina diferentes tecnologias e bancos de dados para entregar uma experiência. Este projeto surgiu a partir do interesse dos integrantes do grupo por academia e bem-estar.

## 🧩 Funcionalidades

### 🍎 Planejamento Alimentar
- Base de Dados Nutricional:
Informações completas sobre alimentos: calorias, macronutrientes e classificação (proteínas, carboidratos, gorduras, etc.).
- Planos Personalizados:
Geração de planos alimentares com base nas metas do usuário (ganho de massa, emagrecimento, manutenção).

## 🏋️ Gestão de Treinos
- Base de Dados de Exercícios:
Informações sobre grupo muscular trabalhado e equipamentos.
- Treinos Personalizados:
Criação de treinos ajustados aos objetivos do usuário.
- Geração Dinâmica de Rotinas:
Sistema monta treinos com base nos grupos musculares e foco.

## 🗄️ Arquitetura & Bancos de Dados
O FitHouse utiliza três bancos de dados para tirar o melhor de cada tecnologia:

- 🐬 MySQL (Relacional):
Armazena dados estruturados e com relações fixas, como cadastros de usuários.

- ⚡ Cassandra (NoSQL - DB1):
Ideal para grandes volumes de dados distribuídos com alta disponibilidade, como planos alimentares personalizados.

- 🍃 MongoDB (NoSQL - DB2):
Ótimo para armazenar dados com estrutura flexível, como treinos mensais.

Essa arquitetura envolve microserviços (S1, S2, S3) e comunicação via Docker e Kafka para garantir escalabilidade e desacoplamento entre os módulos.
A escolha dos bancos de dados foi feita com o propósito de explorar novas tecnologias, pelo menos dois deles são bancos que ainda não foram utilizados pelos integrantes do grupo, permitindo que seja ampliado o conhecimento e experiência na área.  

## 🛠️ Tecnologias Utilizadas
- Backend: Python.
- Integração de Bancos: MySQL, Cassandra e MongoDB.
- Arquitetura: Microserviços + Mensageria (Pub/Sub)

## O que será armazenado no Cassandra (DB1):

-> Gestão de Treinos
- Históricos de treino dos usuários
- Séries e execuções por data
- Consultas rápidas por usuário e período
- Dados densos e com acesso massivo (ex.: treinos do dia)

# 📦 Passo a Passo para Utilização do Docker

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
