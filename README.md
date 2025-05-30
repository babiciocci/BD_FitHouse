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

# 📦 Passo a Passo

## Pré-requisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop) instalado em sua máquina.

## 🚀 Instruções

Assista o vídeo e acompanhe o passo a passo:  [📺 Tutorial](https://www.youtube.com/watch?v=kL_hDxslnS4)

---

1. **Baixe e instale o Docker Desktop**  
   [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

2. **Faça um clone do repositório na sua máquina**:

   ```bash
     git clone https://github.com/NOME-DO-REPOSITÓRIO
   ```

3. **Inicialize os serviços**:

   ```bash
   docker compose --no-cache
   ```

4. **Rode os containers**:

   ```bash
   docker compose up -d
   ```

5. **Crie os databases**
   
   Para criar os bancos, o passo a passo estão localizadas na pasta "Rodar DB". Cada um dos bancos está explicado nos arquivos .txt

6. **Criar as tables e os dados em cada um dos bancos**
   
   Para criar as tables, as queries estão localizadas na pasta "Criar Tables", para cada banco, copiar e colar o código escrito nos arquivos .txt

   Após isso, adicionar os dados em cada banco. Para isso, basta rodar o arquivo "createData.py" para criar dados aleatórios, ou você pode utilizar dos dados já criados como exemplo. Eles estarão nos arquivos que se chama codeNOME-DO-BANCO.txt 

7. **Escrever em "mensagens" quais são os valores que você deseja buscar**

   Localizados no arquivo s1_produtor.py


