import os
import time
from io import StringIO

#Adicionar Cliente:
def adicionar():
    #Variaveis:
    name = input("Digite seu nome: ")
    cpf = input("digite seu CPF: ")
    print(">>>>>> Salário, Comum, Plus <<<<<<")
    Type = input("Qual o tipo da conta: ")
    value = input("Qual o valor inicial da conta: ")
    password = input("Qual a sua senha:")
    
    #Salvando as informações em um "Banco de Dados":
    arq = open( "{}.txt".format(cpf), "w+")
    arq.write("Nome:\n{}\n".format(name))
    arq.write("CPF:\n{}\n".format(cpf))
    arq.write("Tipo de Conta:\n{}\n".format(Type))
    arq.write("Saldo:\n{}\n".format(value))
    arq.write("Senha:\n{}".format(password))
    arq.close()
    
    #Informações para extrato
    arq= open( "{}.txt".format(cpf), "a")
    relogio = time.localtime()
    dia = (relogio.tm_mday)
    mes = (relogio.tm_mon)
    ano = (relogio.tm_year)
    hora = (relogio.tm_hour)
    min = (relogio.tm_min)
    arq.write("\nData: {}/{}/{}             {}:{}                    Sua conta foi criada            Saldo Inicial: {}\n".format(dia,mes,ano,hora,min,value)) 
    arq.close()

#Apagar Cliente:
def apagar():
    CPF = input("Digite o seu CPF:")
    os.remove(CPF+".txt")
    print("Sua conta foi apagada!")

#Debitar:
def debitar():
    try:
        Cpf = input("Digite seu CPF: ")
        arq = open(Cpf+".txt", "r")
        senha = str(input("Qual sua senha: "))
        comp = arq.readlines()
        #Transforma o conteudo de texto em número para poder fazer a debitação de um novo valor:
        if senha+'\n' in comp:
            arq = open(Cpf+".txt","r")
            tipo = str(input("Qual o tipo da sua conta:"))
            comp = arq.readlines()
            nova = float(input("Qual o valor a ser debitar: "))
            if tipo+'\n' in comp:
                if tipo == "Salário":
                    def somatoria(num):
                        S = 0
                        for n in num:
                            float(n)  
                            S = S + float(n)
                        return(S)
                    #Faz a debitação com um número depositado com o número de dentro:          
                    p = nova * 5
                    p2 = p/100
                    final= nova - p2
                    arq = open(Cpf+".txt","r")
                    num = arq.readlines()
                    num_separada = num[7].split()
                    arq.close()
                    teste= (soma2(num_separada))
                    if teste >= 0:
                        if nova <= 500:
                            if teste > -500:   
                                soma= (somatoria(num_separada)) - final
                                print("Foram debitados: %s" %final)
                                saldo5= str(soma)
                                #Criar um buffer temporário para armazenar o conteúdo do arquivo final, substituindo a linha que será alterada:
                                buffer = StringIO()

                                with open(Cpf+".txt", 'r') as stream:
                                    for index, line in enumerate(stream):
                                        #index == 7 representa a linha do arquivo:
                                        buffer.write(saldo5+'\n' if index == 7 else line)

                                with open(Cpf+".txt", 'w') as stream:
                                    stream.write(buffer.getvalue())

                                #Atualização do extrato: 
                                arq = open(Cpf+".txt", "a")
                                relogio = time.localtime()
                                dia = (relogio.tm_mday)
                                mes = (relogio.tm_mon)
                                ano = (relogio.tm_year)
                                hora = (relogio.tm_hour)
                                min = (relogio.tm_min)

                                arq.write("Data: {}/{}/{}       {}:{}      -{}       Tarifa: {}    Saldo: {} \n".format(dia,mes,ano,hora,min,final,p2,soma))
                                arq.close()
                            else:
                                print(">>>>> O seu saldo está mais negativo que o, não poderá debitar! <<<<<<")
                        else:
                            print("O seu saldo está negativo, não poderá debitar!")
                    else:
                        print(">>>>> O seu saldo está mais negativo que o, não poderá debitar! <<<<<<")
                elif tipo == "Comum":
                    def somato(num):
                        S = 0
                        for n in num:
                            float(n)  
                            S = S + float(S)
                        return(S)
                    #Faz a soma com um número depositado com o número de dentro:          
                    p = nova * 3
                    p2 = p/100
                    final= nova - p2
                    arq = open(Cpf+".txt","r")
                    num = arq.readlines()
                    num_separada = num[7].split()
                    arq.close()
                    teste= (soma2(num_separada))
                    if nova <= 500:
                        if teste > -500:
                            soma= (somato(num_separada)) - final
                            print("Foram debitados: %s" %final)
                            saldo3= str(soma)
                            #Criar um buffer temporário para armazenar o conteúdo do arquivo final, substituindo a linha que será alterada:
                            buffer = StringIO()

                            with open(Cpf+".txt", 'r') as stream:
                                for index, line in enumerate(stream):
                                    #index == 7 representa a linha do arquivo:
                                    buffer.write(saldo3+'\n' if index == 7 else line)

                            with open(Cpf+".txt", 'w') as stream:
                                stream.write(buffer.getvalue())

                            #Atualização do extrato: 
                            arq = open(Cpf+".txt", "a")
                            relogio = time.localtime()
                            dia = (relogio.tm_mday)
                            mes = (relogio.tm_mon)
                            ano = (relogio.tm_year)
                            hora = (relogio.tm_hour)
                            min = (relogio.tm_min)

                            arq.write("Data: {}/{}/{}       {}:{}      -{}       Tarifa: {}    Saldo: {} \n".format(dia,mes,ano,hora,min,final,p2,soma))
                            arq.close()
                        else:
                            print(">>>>> O seu saldo está mais negativo que o, não poderá debitar! <<<<<<")
                    else:
                        print("O seu saldo está negativo, não poderá debitar!")
                
                elif tipo == "Plus":
                    def soma2(num):
                        S = 0
                        for n in num:
                            float(n)  
                            S = S + float(n)
                        return(S)
                    #Faz a soma com um número depositado com o número de dentro:          
                    p = nova * 1
                    p2 = p/100
                    final= nova - p2
                    arq = open(Cpf+".txt","r")
                    num = arq.readlines()
                    num_separada = num[7].split()
                    arq.close()
                    teste= (soma2(num_separada))
                    if nova <= 5000:
                        if teste > -5000:
                            soma= (soma2(num_separada))-final
                            print("Foram debitados: %s" %final)
                            saldo4= str(soma)

                            #Criar um buffer temporário para armazenar o conteúdo do arquivo final, substituindo a linha que será alterada:
                            buffer = StringIO()

                            with open(Cpf+".txt", 'r') as stream:
                                for index, line in enumerate(stream):
                                    #index == 7 representa a linha do arquivo:
                                    buffer.write(saldo4+'\n' if index == 7 else line)

                            with open(Cpf+".txt", 'w') as stream:
                                stream.write(buffer.getvalue())

                            #Atualização do extrato: 
                            arq = open(Cpf+".txt", "a")
                            relogio = time.localtime()
                            dia = (relogio.tm_mday)
                            mes = (relogio.tm_mon)
                            ano = (relogio.tm_year)
                            hora = (relogio.tm_hour)
                            min = (relogio.tm_min)

                            arq.write("Data: {}/{}/{}       {}:{}      -{}       Tarifa: {}    Saldo: {} \n".format(dia,mes,ano,hora,min,final,p2,soma))
                            arq.close()
                        else:
                            print(">>>>> O seu saldo está negativo, não poderá debitar! <<<<<<")
                    else:
                        print("Seu saldo não pode ficar menor que 5000")
                else:
                    print("Tipo da conta não condiz com a da conta solicitada")       
            else:
                print("Tipo da conta não condiz com a da conta solicitada")
    except:
        print("Error!")
        
#Depositar:
def depositar():
    try:
        Cpf = input("Digite seu CPF: ")
        #Transforma o conteudo de texto em número para poder fazer a soma de um novo valor:
        def somatoria(num):
            S = 0
            for n in num:
                float(n)  
                S = S + float(n)
            return(S)
        
        #Faz a soma com um número depositado com o número de dentro:    
        arq = open(Cpf+".txt","r")
        nova = int(input("Qual o valor: "))
        num = arq.readlines()
        num_separada = num[7].split()
        arq.close()


        soma= (somatoria(num_separada)) + nova
        print("Foram depositado: %s" %nova)
        saldo2= str(soma)

        #Criar um buffer temporário para armazenar o conteúdo do arquivo final, substituindo a linha que será alterada:
        buffer = StringIO()

        with open(Cpf+".txt", 'r') as stream:
            for index, line in enumerate(stream):
                #index == 7 representa a linha do arquivo:
                buffer.write(saldo2+'\n' if index == 7 else line)

        with open(Cpf+".txt", 'w') as stream:
            stream.write(buffer.getvalue())

        #Atualização do extrato: 
        arq = open(Cpf+".txt", "a")
        relogio = time.localtime()
        dia = (relogio.tm_mday)
        mes = (relogio.tm_mon)
        ano = (relogio.tm_year)
        hora = (relogio.tm_hour)
        min = (relogio.tm_min)

        arq.write("Data: {}/{}/{}       {}:{}      +{}       Tarifa: 0.00    Saldo: {} \n".format(dia,mes,ano,hora,min,nova,soma))
        arq.close() 
    except:
        print("Error!")

#Saldo:
def saldo():
    #Entrando com as variáveis para a entrada do arquivo:
    cpf = input("Digite seu CPF:")
    arq = open(cpf+".txt", "r")

    senha = str(input("Qual sua senha: "))
    comp = arq.readlines()

    #Fazendo comparação para ver se a senha bate com a senha do arquivo:
    if senha+'\n' in comp:
        print("Seu saldo é de: "+ comp[7], end='')
    else:
        print("Senha Errada!")
    arq.close()

#Extrato:
def extrato():
    #Entrando com as variáveis para a entrada do arquivo:
    cpf = input("Digite seu CPF: ")
    archive = open(cpf+".txt", "r")

    #Fazendo comparação para ver se a senha bate com a senha do arquivo:
    senha = str(input("Qual sua senha: "))
    comp = archive.readlines()

    if senha+'\n' in comp:
        #Lendo e separando as linhas para mostrar o extrato
        archive = open(cpf+'.txt', 'r')
        extrato=[]
        for linha in archive.readlines()[11:]:
            linha_separada= linha.split()
            extrato.append(linha_separada)
        print("Aqui está seu Extrato:")
        print(extrato)

        archive.close

#Loop:
opção = 7
while opção != 0:
    print('''    [1] Novo Cliente
    [2] Apagar Cliente
    [3] Debita
    [4] Depositar
    [5] Saldo
    [6] Extrato

    [0] Sair''')
    opção = int(input(">>>>>> Qual sua opção:"))

    #Adicionando novo cliente:
    if opção == 1:
        adicionar()

    #Apagando cliente:
    elif opção == 2:
        apagar()

    #Debitando:
    elif opção == 3:
        debitar()
    
    #Depositar:
    elif opção == 4:
        depositar()

    #Saldo:
    elif opção == 5:
        saldo()
    #Extrato:
    elif opção == 6:
        extrato()
    elif opção == 0:
        print("Obrigado por escolher nossos serviços")
    #Erro:
    else:
        print('Opção inválida. Tente novamente!')
    print("===" * 20)
#Sair:
print("Volte Sempre!")