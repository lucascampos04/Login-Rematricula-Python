import re
import math
import os
#SISTEMA DE LOGIN E CRIAÇÃO DE LOGIN

# VARIAVEIS UTILIZADAS NO CODIGO.

# VARIAVEIS UTILIZADAS NA CRAÇÃO DA TELA DE LOGIN E CRIAÇÃO DA CONTA.
ra = ""
senha = ""
new_user = ""
new_pass = ""

# VATIAVEIS UTILIZAFAS NA CRIAÇÃO DAS INFORMAÇÕES DO USUARIO, BOLETIM E REMATRICULA.
boletim_materias_e_notas = ["Analise de dados:10", "Segurança da informação:10", "Gerencia de Projetos em ti:10", "Desenvolvimento de negocio com agilidade:10", "Projeto em gestão de sistemas:10", "Pssquisa Operacional:10"]

media_notas = sum([10,10,10,10,10,10])


name = "Lucas Oliveira Campos"
cpf = 1010
data_de_nascimento = float(29_06_2004)

confirm_ra = ""
confirm_cpf =""

print("Seja Bem vindo")


# TELA DE FAZER LOGIN E SENHA 
tela_inicial = int(input("1-Login; 2-Criar Conta\n"))

# TELA DE LOGIN._
if tela_inicial == 1:
    while ra != "1234" or senha != "123":
        ra = input("RA:")
        senha = input("Senha:")

        if ra != "1234" or senha!= "123":
            print("Senha ou ra incorreto")
        else:
            print("Login feito com sucesso")
            break
            
    os.system("cls")

    print(f"Olá {ra}")

    tela_usuario = int(input("3-PERFIL; 4-BOLETIM DO SEMSTRE; 5-REMATRICULA\n"))
            

    os.system("cls")
            # CONFIGURAÇÕES DENTRO DA TELA DE USUARIO

            # INFORMAÇÕES DO PERFIL DO USUARIO
    if tela_usuario == 3:
                print("Nome Completo:\n Luacs Oliveira Campos")
                print("Data de Nascimento: 29/06/2004")
                print("Celular: (11) 95073-5140")
                print("CPF: XXXXXX66885")
                print("RG: XXXXX2174")
                print("Nome da mãe: Ednalva Oliveira dos Santos")
                print("Nome do pai: Wellington de Oliveira Santos")
                print("Endereço: Rua Quatorze de Novembro, 11")
                print("Os dados só podem ser alterados na secretaria!!")

            # BOLETIM DO PRIMEIRO SEMESTRE.
    elif tela_usuario == 4:
                print("BOLETIM DO PRIMEIRO SEMESTRE\n")
                
                for boletim_materias_e_notas in boletim_materias_e_notas:
                    print(boletim_materias_e_notas )
                    print("\n")

            # MEDIA DAS NOTAS 
                    print(f"Sua media é:{media_notas}") 
            
if media_notas >= 8:
                print("Parabens você passou de semestre sem pegar nenhuma dp\n")
else:
                print("Você ficou dp\n")

                print("\n")
                
                print("FALTAS: 1\n")

            # REMATRICULA.
if tela_usuario == 5:
                while confirm_ra != ra or confirm_cpf != cpf:
                    confirm_cpf = int(input("Confirme CPF:"))
                    confirm_ra = int(input("Confirme ra:"))

                    if confirm_cpf != "1010" or confirm_ra != "1234":
                        print("Os dados não se coincidem.")
                    else:
                        print("Os dados estão coreetos")
                    os.system("cls")
                    break

                print("QR CODE")
                print("BOLETO\n")

                print("Cartões")
                

# TELA DE CRIAÇÃO DE CONTA.
if tela_inicial == 2:
    while new_user != "Usuario" or new_pass != input("Senha:"):
        new_user = input("Usuario:")
        new_pass = input("Senha:")
        confirm_pass = input("Confirmar senha:")

        if confirm_pass != new_pass:
            print("As senhas não se coincidem")
        else:
            print("Conta criada com sucesso")
            os.system("cls")
            print("Olá", new_user)
            break

        
            
    



