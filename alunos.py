import os
import json
import time

nome_do_arquivo = "alunos.json"

def lerArquivo() -> list:
    arq = open(nome_do_arquivo,'r', encoding='utf-8')
    data = arq.read()
    return json.loads(data)

def salvar_arquivo(alunos :dict):
     arq = open(nome_do_arquivo, 'w+', encoding='utf-8')
     data = json.dumps(alunos, indent=4)
     arq.write(data)
     arq.close()

class Cadastra():
    def cadastraraluno(self) -> dict:
            print("---------- Vamos cadastra o aluno ----------")
            aluno = {}
            aluno['Nome'] = input("Digite o nome do Aluno: ")
            aluno['CPF'] = str(input("Digite o numero do CPF do Aluno: "))
            aluno['Matricula'] = str(input("Digite o numero da Matricula do Aluno: "))
            aluno['Endereço'] = str(input("Digite o Endereço do Aluno: "))
            aluno['Telefone'] = str(input("Digite o Numero do Aluno: "))

            alunos = lerArquivo()
            alunos.append(aluno)
            salvar_arquivo(alunos)
            print("--- Aluno cadastrado com sucesso!...")
            time.sleep(3)

class Altera():
    def alteraraluno(self):
            print("---------- Alteração do aluno ----------")
            alunos = lerArquivo()
            cpf = str(input("Digite o CPF do aluno que deseja alterar: "))
            
            print("--- Verificando o aluno!...")
            achou = False
            for aluno in alunos:
                if cpf == aluno["CPF"]:
                    achou = True
                    indexaluno = alunos.index(aluno)
                    aluno["Nome"] = input("Digite o nome do Aluno: ")
                    aluno["CPF"] = str(input("Digite o numero do CPF do Aluno: "))
                    aluno["Matricula"] = str(input("Digite o numero da Matricula do Aluno: "))
                    aluno["Endereço"] = str(input("Digite o Endereço do Aluno: "))
                    aluno["Telefone"] = str(input("Digite o Numero do Aluno: "))
                    
                    alunos[indexaluno] = aluno
                    salvar_arquivo(alunos)
                    print("--- Aluno alterado com sucesso!...")
                    time.sleep(3)

            if not achou:
                print("--- Por favor digite um cpf valido!...")
                time.sleep(3)
class Deletar():
    def deletaraluno(self):   
            print("---------- Deletar o aluno ----------")
            alunos = lerArquivo()
            nome_aluno = str(input("Digite o nome do aluno que deseja deletar: "))
            verificando = False
            for aluno in alunos:
                if nome_aluno == aluno["Nome"]:
                    alunos.remove(aluno)
                    salvar_arquivo(alunos)
                    print('--- Aluno deletado com sucesso!...')
                    time.sleep(3)
                
                   
                    verificando = True


            print('--- Carregando!...')
            time.sleep(2)

            if not verificando:      
                print("-- Nenhum aluno encontrado no nosso banco de dados!...")
                time.sleep(3)
                    

            input("Digite enter para continuar")
            os.system('clear' if os.name == "posix" else 'cls')
            print("---------- Continuando com o cadastro ----------")
            print("Carregando...")
            time.sleep(3)

class Selecionar():
    def selecionarmatricula(self):
            print("---------- Selecione um alunos ----------")
            alunos = lerArquivo()
            matricula = str(input("Digite a matricula do Aluno que você deseja verificar: "))
            for aluno in alunos:
                if matricula == aluno['Matricula']:
                    print(aluno)
                    time.sleep(3)
                    salvar_arquivo(alunos)
                    print("--- Continuando com o cadastro!...")

                else:
                    print("--- Carrgando...!")
                    print("--- Nunhum aluno foi encontrado...!")
                    time.sleep(2)



def selecionartodos():     
        print("---------- Todos os alunos ----------")
        arq = open(nome_do_arquivo)
        linhas = arq.read()
        linhas = json.loads(linhas)
        for linha in linhas:
            print(linha["Nome"])
            print(linha["CPF"])
            print(linha["Matricula"])
            print(linha["Endereço"])
            print(linha["Telefone"])

            time.sleep(2)

def menu():
    print('-=--=--=--=--=- Sistema de cadastro de alunos -=--=--=--=--=-')
    print('1 - Cadastrar Aluno')
    print('2 - Alterar Aluno')
    print('3 - Deletar Aluno')
    print('4 - Selecionar pela Matricula')
    print('5 - Selecionar Todos')
    print('6 - Sair')
    print(21 * '-=-')
    return int(input('Escolha uma opção: '))