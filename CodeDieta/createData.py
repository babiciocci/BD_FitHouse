# Projeto: FitStore
# Feito por: Bruno Arthur Basso Silva 
#            Gabriela Molina Ciocci
# RA:        22.123.067-5 
#            22.222.032-9
# Disciplina: CC6240 - Tópico Avançado de Banco de Dados
# Coordenador(a): Leonardo Anjoletto Ferr
# eira
# Ciclo: 6° Semestre. 
# Curso: Ciência da Computação
# Universidade: Centro Universitário FEI

# Para começar o projeto, primeiro precisamos importar todas as bibliotecas que iremos utilizar.

import random

# Utilizamos a biblioteca random para poder criar valores randômicos.

# Abrimos os arquivos onde contém os dados.
# OBS: não esqueça de verificar se os arquivos estão na mesma pasta do programa!

archive_user = open("usuarios.txt", "r")
archive_user_read = archive_user.read()
archive_user.close()

archive_breakfest = open("breakfest.txt", "r")
archive_breakfest_read = archive_breakfest.read()
archive_breakfest.close()

archive_lunch = open("lunch.txt", "r")
archive_lunch_read = archive_lunch.read()
archive_lunch.close()

archive_dinner = open("dinner.txt", "r")
archive_dinner_read = archive_dinner.read()
archive_dinner.close()

archive_snacks = open("snack.txt", "r")
archive_snacks_read = archive_snacks.read()
archive_snacks.close()

archive_suppers = open("supper.txt", "r")
archive_suppers_read = archive_suppers.read()
archive_suppers.close()

# archive_store = open("produtos.txt", "r")
# archive_store_read = archive_store.read()
# archive_store.close()

# archive_exercises = open("exercicios.txt", "r")
# archive_exercises_read = archive_exercises.read()
# archive_exercises.close()

# Formatação dos arquivos para facilitar o processo de criação dos itens.

archive_user_read = archive_user_read.split("\n")
archive_breakfest_read = archive_breakfest_read.split("\n\n")
archive_lunch_read = archive_lunch_read.split("\n\n")
archive_dinner_read = archive_dinner_read.split("\n\n")
archive_snacks_read = archive_snacks_read.split("\n\n")
archive_suppers_read = archive_suppers_read.split("\n\n")
# archive_store_read = archive_store_read.split("\n")
# archive_exercises_read = archive_exercises_read.split("\n")


# Lista que será responsável por armazenar os valores de ID existentes no programa.

existingID = []

# Lista que será responsável por armazenar os 

peoples = []
users = []
products = []
breakfests = []
lunchs = []
dinners = []
snacks = []
suppers = []
diets = []
exercises = []
diet_users = []
workout_user = []

# Formatação dos arquivos de dieta para facilitar o processo de criação. 

for ref in archive_breakfest_read:
    ref = ref.split("\n")
    breakfests.append(ref)

for ref in archive_lunch_read:
    ref = ref.split("\n")
    lunchs.append(ref)

for ref in archive_dinner_read:
    ref = ref.split("\n")
    dinners.append(ref)

for ref in archive_snacks_read:
    ref = ref.split("\n")
    snacks.append(ref)

for ref in archive_suppers_read:
    ref = ref.split("\n")
    suppers.append(ref)

for data in archive_user_read:
    data = data.split(", ")
    peoples.append(data)

# Função responsável por criar as datas em dia, mês e ano.

def createDate(type):
    day = random.randint(1, 28)
    mounth = random.randint(1, 12)

    if day < 10:
        day = "0" + str(day)
    if mounth < 10:
        mounth = "0" + str(mounth)

    # Tipo 1: para datas de nascimento.
    if type == 1:
        year = random.randint(1950, 2005)
    
    # Tipo 2: para datas de aquisição
    if type == 2:
        year = random.randint(2024, 2025)

    return day, mounth, year


# Aqui estão loaclizadas as funções necessárias para que o programa possa ser executado com êxito.
# createUser: Cria um usuário.
# Começamos gerando um ID de usuário aleatório. Utilizamos random para gerar um número aleatório de 0 até o comprimento do arquivo
# de usuários e fazemos a comparação com os ID's existentes para evitar IDs duplicados. Enquanto o valor do ID existir na lista de
# ID's existentes, o programa irá alterar o valor. 

def createUser():
    user_id = random.randint(0, len(peoples) - 1)
    while user_id in existingID:
        user_id = random.randint(0, len(peoples) - 1)

    # Obtém o nome do usuário a partir do arquivo de nomes usando o user_id gerado.
    name = peoples[user_id][0]
    # Cria uma data de registro chamando a função createDate.
    born_date = createDate(1)
    # Obtém o foco do usuário a partir do arquivo de nomes usando o user_id gerado.
    focus_user = peoples[user_id][1]

    # Adiciona o ID do usuário à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(user_id)
    # Adiciona os detalhes do usuário na lista de usuários. As listas finais serão a dieta e o treino.
    users.append([user_id, name, born_date, focus_user, [], []])
    # Retorna o ID, nome e data de registro do usuário recém-criado. Não é necessário, mas foi colocado para manter 
    # formalidade no código.
    return user_id, name, born_date

# createProduct: Cria um produto.
# Iniciamos novamente a geração de um ID de jogo aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor. 
# No final, somamos 50 com o resultado apenas para padronização e identificação de ID's de produtos.

def createProduct(archive):
    product_id = random.randint(0, len(archive) - 1) + 50
    while product_id in existingID:
        product_id = random.randint(0, len(archive) - 1) + 50

    # Obtém o nome do produto a partir do arquivo de produtos usando o id gerado.
    title = archive[product_id - 50][0]
    # Obtém o nome da marca.
    mark = archive[product_id - 50][1]
    # Obtém o preço do produto.
    price = archive[product_id - 50][2]
    # Adiciona o ID do produto à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(product_id)
    # Adiciona os detalhes do produto na lista de produtos.
    products.append([product_id, title, mark, price])
    # Retorna o ID, nome e data de lançamento do produto recém-criado. Não é necessário, mas foi colocado para manter formalidade 
    # no código.
    return product_id, title, mark, price

# createExercise: Cria um exercício.
# Iniciamos novamente a geração de um ID de conquista aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para conquistas são de valores maiores que 600.

def createExercise(archive):
    exercise_id = random.randint(0, len(archive) - 1) + 600
    while exercise_id in existingID:
        exercise_id = random.randint(0, len(archive) - 1) + 600

    # Obtém o nome do exercício a partir do arquivo de exercícios usando o exercise_id gerado.
    name = archive[exercise_id - 600][0]
    # Obtém o grupo muscular do exercício a partir do arquivo de exercícios usando o exercise_id gerado.
    muscle_group_exercise = archive[exercise_id - 600][1]
    # Obtém o foco muscular do exercício a partir do arquivo de exercícios usando o exercise_id gerado.
    muscle_focus_exercise = archive[exercise_id - 600][2]

    # Adiciona o ID da conquista à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(exercise_id)
    # Adiciona os detalhes da conquista na lista de conquistas.
    exercises.append([exercise_id, name, muscle_group_exercise, muscle_focus_exercise])
    # Retorna o ID, título e jogo da conquista recém-criada.
    return exercise_id, name, muscle_group_exercise, muscle_focus_exercise

# createDiet: Cria um cardápio.
# Iniciamos novamente a geração de um ID de dieta aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para conquistas são de valores maiores que 1000.

def createDiet(focus):
    diet_id = random.randint(1000, 1500)
    while diet_id in existingID:
        diet_id = random.randint(1000, 1500)

    if(focus == "hypertrophy"):
        breakfest = breakfests[random.randint(0, len(breakfests) - 1)]
        lunch = lunchs[random.randint(0, len(lunchs) - 1)]
        snack = snacks[random.randint(0, len(snacks) - 1)]
        dinner = dinners[random.randint(0, len(dinners) - 1)]
        supper = suppers[random.randint(0, len(suppers) - 1)]
        # Adiciona os detalhes do cardápio na lista de dietas.
        diets.append([diet_id, "hypertrophy", breakfest, lunch, snack, dinner, supper])

    # Adiciona o ID da dieta à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(diet_id)
    # Retorna o ID e os itens da dieta.
    return breakfest, lunch, snack, dinner, supper

# createDietUser: Cria uma dieta para o usuário.
# O ID padronizado para dietas são de valores maiores que 1000 e menores que 2500.

def createDietUser():
    dietUser_id = random.randint(2000, 2500)
    while dietUser_id in existingID:
        dietUser_id = random.randint(2000, 2500)

    # Obtemos um usuário existente para adicionar uma dieta.
    user = users[random.randint(0, len(users) - 1)]
    # Obtemos o id do usuário.
    user_id = user[0]
    # Obtemos o foco do usuário.
    user_focus = user[3]
    # Obtemos uma dieta.
    diet = diets[random.randint(0, len(diets) - 1)]
    # Obtemos o id da dieta.
    diet_id = diet[0]

    if (user_focus == "hypertrophy"):
        while diet[1] != "hypertrophy":
            diet = diets[random.randint(0, len(diets) - 1)]

        if len(user[4]) != 0:
            user[4] = []
        user[4].append(diet)
    
    # Adiciona o ID da música da playlist à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(dietUser_id)
    # Adiciona os detalhes da dieta do usuário na lista de dietas de usuário.
    diet_users.append([dietUser_id, diet_id, user_id])
    # Retorna o ID do usuário, o ID do uduário e o ID da dieta.
    return dietUser_id, diet_id, user_id


def printAllItems():
    for i in users:
        print("Usuário:     ", i)
    print()
    for i in diets:
        print("Dieta:     ", i)
    print()
    for i in diet_users:
        print("Dieta do usuário:     ", i)
    print()

# Função responsável por gerar o arquivo txt que contém os códigos SQL para adicionar todos os itens no banco de dados.
# O nome do arquivo gerado será "codeDieta.txt" e será encontrado na mesma pasta em que o programa está localizado.

def createExportCode(users, diets, diet_users):
    code_archive = open("codeDieta.txt", "w")
    code_archive.write("DELETE FROM dieta_usuario;\n")
    code_archive.write("DELETE FROM dieta;\n")
    code_archive.write("DELETE FROM usuario;\n")

    # QUERYS ANTERIORES:
    # for i in users:
    #     code_archive.write("INSERT INTO usuario (id, nome, data_registro, foco) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + str(i[2][2]) + "-" + str(i[2][1]) + "-" + str(i[2][0]) + "', '" + i[3] + "');\n")

    # for i in diets:
    #     code_archive.write("INSERT INTO dieta (id, tipo_dieta, cafe_manha, almoco, cafe_tarde, jantar, ceia) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + str(i[2]) + "', '" + str(i[3]) + "', '" + str(i[4]) + "', '" + str(i[5]) + "', '" + str(i[6]) + "');\n")

    # for i in diet_users:
    #     code_archive.write("INSERT INTO dieta_usuario (id, id_dieta, id_usuario) VALUES (" + str(i[0]) + ", '" + str(i[1]) + "', '" + str(i[2]) + "');\n")

    # CASO DE ERRADO AJEITE AS QUERYS AQ
    for i in users:
        code_archive.write("INSERT INTO usuario (id, nome, data_registro, foco) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + str(i[2][0]) + "-" + str(i[2][1]).zfill(2) + "-" + str(i[2][2]).zfill(2) + "', '" + i[3] + "');\n")

    for i in diets:
        code_archive.write("INSERT INTO dieta (id, tipo_dieta, cafe_manha, almoco, cafe_tarde, jantar, ceia) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + str(i[2]) + "', '" + str(i[3]) + "', '" + str(i[4]) + "', '" + str(i[5]) + "', '" + str(i[6]) + "');\n")

    for i in diet_users:
        code_archive.write("INSERT INTO dieta_usuario (id, id_dieta, id_usuario) VALUES (" + str(i[0]) + ", " + str(i[1]) + ", " + str(i[2]) + ");\n")

    code_archive.close()
    print("---> Dados gerados com sucesso!")
    print("---> Nome do arquivo: codeDieta.txt")


# Menu para o terminal. Apenas para fins estéticos do código, não altera a lógica do programa.

def menu():
    print("|=================================================|")
    print("|                    FitStore                     |")
    print("|=================================================|")
    print()
    print("|=====================[INFOS]=====================|")
    print("| Ciclo: 6° semestre                              |")
    print("| Curso: Ciência da Computação - FEI              |")
    print("| Disciplina: CC5232 - Banco de Dados             |")
    print("| Data: 16/05/2025                                |")
    print("|=================================================|")
    print()
    print("|================[DESENVOLVEDORES]================|")
    print("| Nomes: Bruno Arthur Basso Silva                 |")
    print("|        Gabriela Molina Ciocci                   |")
    print("| RA:    22.123.067-5                             |")
    print("|        22.222.032-9                             |")
    print("|=================================================|")
    print()
    print("|=================================================|")
    print("|            Aperte enter para iniciar!           |")
    print("|=================================================|")

# Função principal do programa.
# Aqui é onde toda a lógica é criada. 

def main():
    for _ in range(0, num_users):
        createUser()
    for _ in range(0, num_diets):
        createDiet("hypertrophy")
    for _ in range(0, num_dietUsers):
        createDietUser()

    # printAllItems()

    createExportCode(users, diets, diet_users)


# Função de início do programa
def start():

    menu()
    input()
    main()

    print("Obrigado por utilizar!")
    print()

# Variáveis responsáveis por informar a quantidade de cada item o usuário gostaria de criar.
num_users = 32
num_diets = 80

num_dietUsers = 10

start()