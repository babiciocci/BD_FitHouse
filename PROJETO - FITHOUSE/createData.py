# Projeto: FitHouse
# Feito por: Bruno Arthur Basso Silva 
#            Gabriela Molina Ciocci
# RA:        22.123.067-5 
#            22.222.032-9
# Disciplina: CC6240 - Tópico Avançado de Banco de Dados
# Coordenador(a): Leonardo Anjoletto Ferreira
# Ciclo: 6° Semestre. 
# Curso: Ciência da Computação
# Universidade: Centro Universitário FEI

# Para começar o projeto, primeiro precisamos importar todas as bibliotecas que iremos utilizar.
# Utilizamos a biblioteca random para poder criar valores randômicos.

import random

# Abrimos os arquivos onde contem os dados.
# OBS: não esqueça de verificar se os arquivos estão na mesma pasta do programa!

archive_user = open("files/usuarios.txt", "r")
archive_user_read = archive_user.read()
archive_user.close()

archive_breakfest = open("files/breakfest.txt", "r")
archive_breakfest_read = archive_breakfest.read()
archive_breakfest.close()

archive_lunch = open("files/lunch.txt", "r")
archive_lunch_read = archive_lunch.read()
archive_lunch.close()

archive_dinner = open("files/dinner.txt", "r")
archive_dinner_read = archive_dinner.read()
archive_dinner.close()

archive_snacks = open("files/snack.txt", "r")
archive_snacks_read = archive_snacks.read()
archive_snacks.close()

archive_suppers = open("files/supper.txt", "r")
archive_suppers_read = archive_suppers.read()
archive_suppers.close()

archive_exercises = open("files/exercises.txt", "r")
archive_exercises_read = archive_exercises.read()
archive_exercises.close()

# Formatação dos arquivos para facilitar o processo de criação dos itens.

archive_user_read = archive_user_read.split("\n")
archive_breakfest_read = archive_breakfest_read.split("\n\n")
archive_lunch_read = archive_lunch_read.split("\n\n")
archive_dinner_read = archive_dinner_read.split("\n\n")
archive_snacks_read = archive_snacks_read.split("\n\n")
archive_suppers_read = archive_suppers_read.split("\n\n")
archive_exercises_read = archive_exercises_read.split("\n")


# Lista que será responsável por armazenar os valores de ID existentes no programa.

existingID = []

# Lista que será responsável por armazenar todos os elementos do programa.

peoples = []
users = []

breakfests = []
lunchs = []
dinners = []
snacks = []
suppers = []
diets = []
diet_users = []

exercises_inf = []
exercises_sup = []
exercises_abs = []
exercises_cardio = []

workouts = []
workout_user = []

qty_rep = ['3 series de 12', '3 series de 15', '3 series de 10', '4 series de 12', '4 series de 10', '3 series de 8 (carga elevada)', 
           '5 series de 10 (15s de desncanso)','4 series (20, 15, 12, 10) aumentando peso', '3 series de 8x8x8 (dropset)', 
           '4 series de 8x8x8 (dropset)', '3 series de 20 (demorando 3s pra descer e 2s pra subir)', '2 series de 15, 2 series ate a falha']

qty_cardio = ['30min, intensidade alta(1min) intensidade media (1min)', '30min, intensidade alta(2min) intensidade media (1min)', 
              '40min, intensidade alta(1min) intensidade media (1min)', '40min, intensidade alta(2min) intensidade media (1min)', 
              '20min, intensidade alta(2min) intensidade media (1min)', '1h intensidade alta(1min) intensidade media (1min)']

# Formatação dos arquivos de dieta e exercícios para facilitar o processo de criação. 

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

for exercise in archive_exercises_read:
    exercise = exercise.split(", ")
    if(exercise[1] == "Inferiores"):
        exercises_inf.append(exercise)
    if(exercise[1] == "Superiores"):
        exercises_sup.append(exercise)
    if(exercise[1] == "Abdominais"):
        exercises_abs.append(exercise)
    if(exercise[1] == "Cardio"):
        exercises_cardio.append(exercise)

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

    return day, mounth, year


# Aqui estão loaclizadas as funções necessárias para que o programa possa ser executado com êxito.
# createUser: Cria um usuário.
# Começamos gerando um ID de usuário aleatório. Utilizamos random para gerar um número aleatório de 0 ate o comprimento do arquivo
# de usuários e fazemos a comparação com os ID's existentes para evitar IDs duplicados. Enquanto o valor do ID existir na lista de
# ID's existentes, o programa irá alterar o valor. 

def createUser():
    user_id = random.randint(0, len(peoples) - 1)
    while user_id in existingID:
        user_id = random.randint(0, len(peoples) - 1)

    # Obtem o nome do usuário a partir do arquivo de nomes usando o user_id gerado.
    name = peoples[user_id][0]
    # Cria uma data de registro chamando a função createDate.
    born_date = createDate(1)
    # Obtem o foco do usuário a partir do arquivo de nomes usando o user_id gerado.
    focus_user = peoples[user_id][1]

    # Adiciona o ID do usuário à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(user_id)
    # Adiciona os detalhes do usuário na lista de usuários. As listas finais serão a dieta e o treino.
    users.append([user_id, name, born_date, focus_user, [], []])
    # Retorna o ID, nome e data de registro do usuário recem-criado. Não e necessário, mas foi colocado para manter 
    # formalidade no código.
    return user_id, name, born_date

# createExercise: Cria um exercício.
# Iniciamos novamente a geração de um ID de conquista aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para conquistas são de valores maiores que 600.

def createWorkout(type):
    workout_id = random.randint(600, 1000)
    while workout_id in existingID:
        workout_id = random.randint(600, 1000)

    workout = []

    # Obtemos um conjunto de exercícios para criar um treino.
    # Se for cardio, só um basta pro dia.
    if type == "cardio":
            exercise = exercises_cardio[random.randint(0, len(exercises_cardio) - 1)]
            qty_cardio_temp = qty_cardio[random.randint(0, len(qty_cardio) - 1)]
            workout.append([exercise, qty_cardio_temp])
    else:
        for exercise in range(0, 5):
            if type == "inf":
                exercise = exercises_inf[random.randint(0, len(exercises_inf) - 1)]
                qty_rep_temp = qty_rep[random.randint(0, len(qty_rep) - 1)]
                workout.append([exercise, qty_rep_temp])
            if type == "sup":
                exercise = exercises_sup[random.randint(0, len(exercises_sup) - 1)]
                qty_rep_temp = qty_rep[random.randint(0, len(qty_rep) - 1)]
                workout.append([exercise, qty_rep_temp])
            if type == "abs":
                exercise = exercises_abs[random.randint(0, len(exercises_abs) - 1)]
                qty_rep_temp = qty_rep[random.randint(0, len(qty_rep) - 1)]
                workout.append([exercise, qty_rep_temp])
            
    # Adiciona o ID à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(workout_id)
    # Adiciona os detalhes da dieta do usuário na lista de dietas de usuário.
    workouts.append([workout_id, workout])
    # Retorna o ID do usuário, o ID do uduário e o ID da dieta.
    return workout_id, workout

# createExercise: Cria um exercício.
# Iniciamos novamente a geração de um ID de conquista aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para conquistas são de valores maiores que 3000.

def createWorkoutUser():
    workoutUser_id = random.randint(3000, 3500)
    while workoutUser_id in existingID:
        workoutUser_id = random.randint(3000, 3500)

    # Obtemos um usuário existente para adicionar uma dieta.
    user = users[random.randint(0, len(users) - 1)]
    # Obtemos o id do usuário.
    user_id = user[0]
    # Criamos uma lista temporária que conterá os treinos semanais do usuário.
    workout_user_temp = []
    # Obtemos um treino existente para adicionar um treino.
    for qtd in range(0, 6):
        workout = workouts[random.randint(0, len(workouts) - 1)]
        
        if qtd == 0:
            while workout[1][0][0][1] != "Inferiores":
                workout = workouts[random.randint(0, len(workouts) - 1)]
        if qtd == 1:
            while workout[1][0][0][1] != "Superiores":
                workout = workouts[random.randint(0, len(workouts) - 1)]
        if qtd == 2:
            while workout[1][0][0][1] != "Abdominais":
                workout = workouts[random.randint(0, len(workouts) - 1)]
        if qtd == 3:
            while workout[1][0][0][1] != "Inferiores":
                workout = workouts[random.randint(0, len(workouts) - 1)]
        if qtd == 4:
            while workout[1][0][0][1] != "Superiores":
                workout = workouts[random.randint(0, len(workouts) - 1)]
        if qtd == 5:
            while workout[1][0][0][1] != "Cardio":
                workout = workouts[random.randint(0, len(workouts) - 1)]

        # Obtemos o id do treino.
        workout_id = workout[0]
        # Adiciona os detalhes do treino do usuário na lista temporária de treino.
        workout_user_temp.append(workout_id)

    # Adiciona o ID do treino à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(workoutUser_id)
    # Adiciona os detalhes da dieta do usuário na lista de dietas de usuário.
    workout_user.append([workoutUser_id, user_id, workout_id, workout_user_temp])

    user[5].append(workout_user_temp)
    # Retorna o ID do treino do usuário, o ID do usuário e o ID do treino.
    return workoutUser_id, user_id, workout_id

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
# O ID padronizado para dietas são de valores maiores que 2000 e menores que 2500.

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
    
    # Adiciona o ID à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(dietUser_id)
    # Adiciona os detalhes da dieta do usuário na lista de dietas de usuário.
    diet_users.append([dietUser_id, diet_id, user_id])
    # Retorna o ID da dieta do usuário, o ID da dieta e o ID do usuário.
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
    for i in workouts:
        print("Treinos:     ", i)
    print()
    for i in workout_user:
        print("Treinos de usuário:     ", i)
    print()

# Função responsável por gerar o arquivo txt que contem os códigos para adicionar todos os itens no banco de dados.
# O nome do arquivo gerado será "codeMySQL.txt" e será encontrado na mesma pasta em que o programa está localizado.
# Banco de dados: MySQL.

def createExportCodeMySQL(users):
    code_archive = open("codeMySQL.txt", "w")
    code_archive.write("DELETE FROM usuario;\n")

    for i in users:
        code_archive.write("INSERT INTO usuario (id, nome, data_registro, foco) VALUES (" 
                           + str(i[0]) + ", '"
                           + i[1] + "', '" 
                           + str(i[2][2]) + "-" 
                           + str(i[2][1]) + "-" 
                           + str(i[2][0]) + "', '" 
                           + i[3] + "');\n")

    code_archive.close()
    print("---> Dados MySQL gerados com sucesso!")
    print("---> Nome do arquivo: codeMySQL.txt")

# Função responsável por gerar o arquivo txt que contem os códigos para adicionar todos os itens no banco de dados.
# O nome do arquivo gerado será "codeCassandra.txt" e será encontrado na mesma pasta em que o programa está localizado.
# Banco de dados: Cassandra.

def createExportCodeCassandra(diets, diet_users):
    code_archive = open("codeCassandra.txt", "w")
    code_archive.write("TRUNCATE dieta_usuario;\n")
    code_archive.write("TRUNCATE dieta;\n")

    for i in diets:
        print(", ".join(i[2]))
        code_archive.write("INSERT INTO dieta (id, tipo_dieta, cafe_manha, almoco, cafe_tarde, jantar, ceia) VALUES (" 
                       + str(i[0]) + ", '" 
                       + i[1] 
                       + "', [" + ", ".join("'" + item + "'" for item in i[2]) + "], "
                       + "[" + ", ".join("'" + item + "'" for item in i[3]) + "], "
                       + "[" + ", ".join("'" + item + "'" for item in i[4]) + "], "
                       + "[" + ", ".join("'" + item + "'" for item in i[5]) + "], "
                       + "[" + ", ".join("'" + item + "'" for item in i[6]) + "]);\n")

    for i in diet_users:
        code_archive.write("INSERT INTO dieta_usuario (id, id_dieta, id_usuario) VALUES (" 
                           + str(i[0]) + ", " 
                           + str(i[1]) + ", " 
                           + str(i[2]) + ");\n")

    code_archive.close()
    print("---> Dados Cassandra gerados com sucesso!")
    print("---> Nome do arquivo: codeCassandra.txt")

# Função responsável por gerar o arquivo txt que contem os códigos para adicionar todos os itens no banco de dados.
# O nome do arquivo gerado será "codeMongoDB.txt" e será encontrado na mesma pasta em que o programa está localizado.
# Banco de dados: MongoDB.

def createExportCodeMongoDB(workouts, workout_users):
    code_archive = open("codeMongoDB.txt", "w")
    code_archive.write("db.treino_usuario.deleteMany({});\n")
    code_archive.write("db.treino.deleteMany({});\n")

    for i in workouts:
        if len(i[1]) == 5:
            doc = {
                "id": i[0],
                "exercise_1": f"{i[1][0][0][0]}, {i[1][0][1]}",
                "exercise_2": f"{i[1][1][0][0]}, {i[1][1][1]}",
                "exercise_3": f"{i[1][2][0][0]}, {i[1][2][1]}",
                "exercise_4": f"{i[1][3][0][0]}, {i[1][3][1]}",
                "exercise_5": f"{i[1][4][0][0]}, {i[1][4][1]}",
                "exercise_cardio": "null"
            }
        else:
            doc = {
                "id": i[0],
                "exercise_1": "null",
                "exercise_2": "null",
                "exercise_3": "null",
                "exercise_4": "null",
                "exercise_5": "null",
                "exercise_cardio": f"{i[1][0][0][0]}, {i[1][0][1]}"
            }
        code_archive.write(f"db.treino.insertOne({doc});\n")

    for i in workout_users:
        doc = {
            "id": i[0],
            "id_usuario": i[1],
            "id_treino": i[2],
            "treino_seg": i[3][0],
            "treino_ter": i[3][1],
            "treino_qua": i[3][2],
            "treino_qui": i[3][3],
            "treino_sex": i[3][4],
            "treino_sab": i[3][5] 
        }

        code_archive.write(f"db.treino_usuario.insertOne({doc});\n")

    print("---> Dados MongoDB gerados com sucesso!")
    print("---> Nome do arquivo: codeMongoDB.txt")


# Menu para o terminal. Apenas para fins esteticos do código, não altera a lógica do programa.

def menu():
    print("|=================================================|")
    print("| FitHouse - Sistema p/ Gestão de Treinos e Dieta |")
    print("|=================================================|")
    print()
    print("|=====================[INFOS]=====================|")
    print("| Ciclo: 6° semestre                              |")
    print("| Curso: Ciência da Computação - FEI              |")
    print("| Disciplina: CC6240 - Tópicos Avançados de BD    |")
    print("| Data: 24/05/2025                                |")
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
# Aqui é onde toda a lógica e criada. 

def main():
    for _ in range(0, num_users):
        createUser()
    for _ in range(0, num_diets):
        createDiet("hypertrophy")
    for _ in range(0, num_dietUsers):
        createDietUser()
    for _ in range(0, num_diets):
        createDiet("hypertrophy")
    for _ in range(0, int(num_workouts/4)):
        createWorkout("inf")
    for _ in range(0, int(num_workouts/4)):
        createWorkout("sup")
    for _ in range(0, int(num_workouts/4)):
        createWorkout("abs")
    for _ in range(0, int(num_workouts/4)):
        createWorkout("cardio")
    for _ in range(0, num_workoutsUser):
        createWorkoutUser()

    # printAllItems()

    createExportCodeMySQL(users)
    print()
    createExportCodeMongoDB(workouts, workout_user)
    print()
    createExportCodeCassandra(diets, diet_users)


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
num_exercises = 30
num_workouts = 20

num_workoutsUser = 32
num_dietUsers = 10

# Iniciando o programa.
start()