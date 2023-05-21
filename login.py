import math
import os 
# SISTEMA DE REMATRICULA 

def matricula_escola():
    inicial = input("[1] - Login | [2] - Fazer Matricula : ")

    if inicial == '1':
        ra = input("Insira seu RA: ")
        confirm_ra = input("Confirme o RA: ")
        if ra == confirm_ra:
            senha = input("Insira sua senha: ")
            confirm_senha = input("Confirme a senha: ")
            if senha == confirm_senha:
                pass
                os.system('cls')
            else:
                print("As senhas não estão iguais.")
                return matricula_escola()
        else:
            print("Os RA não está iguais")
            return matricula_escola()
        
        if ra == 'admin' and senha == '123':

            print("Olá", ra)
            perfil = input("[1] - Dados Pessoais \n[2] - Notas \n[3] - Ocorrencias \n[4] - Rematricula: ")

            if perfil == '1':
                dados_pessoais = print("Nome: Lucas Olivera Campos \nData de nascimento: 29/06/2004 \nCPF: XXXXXXXX \nRG: XXXXXXXX, \nTelefone: Celular: (11) 95073-5140 \nNome da mãe: Ednalva Oliveira dos Santos \nNome do pai: Wellington de Oliveira Santos \nEndereço: Rua Quatorze de Novembro, 11 \nOs dados só podem ser alterados na secretaria" )
            elif perfil == '2':
                notas = print("Analise de dados:10 \nSegurança da informação:10 \nGerencia de Projetos em ti:10 \nDesenvolvimento de negocio com agilidade:10 \nProjeto em gestão de sistemas:10 \nPssquisa Operacional:10")
                
                media = (10*6)/6
                print("A sua média é: ", media)

            elif perfil == '3':
                ocorrencias = print("O usuario não tem nenhuma ocorrencia")

            elif perfil == '4':
                cpf = input("CPF: ")
                confirm_cpf = input("COnfirme o cpf: ")

                if cpf == confirm_cpf:
                    modo_de_pagamento = input("[1] - Cartão de credito \n[2] - Cratão de debito \n[3] - Pix \n[4] - Boleto: ")

                    if modo_de_pagamento == '1':
                        cartao_credito = input("Digite o número do cartão de crédito: ")
                        validade = input("Digite a validade do cartão (MM/AA): ")
                        codigo_seguranca = input("Digite o código de segurança do cartão: ")
                        print("Pagamento com cartão de crédito realizado com sucesso!")

                    elif modo_de_pagamento == '2':
                        cartao_debito = input("Digite o número do cartão de débito: ")
                        senha = input("Digite a senha do cartão: ")
                        print("Pagamento com cartão de débito realizado com sucesso!")

                    elif modo_de_pagamento == '3':
                        chave_pix = input("Digite a chave PIX: ")
                        valor = float(input("Digite o valor da transação: "))
                        print("Pagamento com PIX realizado com sucesso!")

                    elif modo_de_pagamento == '4':
                        boleto = input("Digite o código de barras do boleto: ")
                        print("Pagamento com boleto realizado com sucesso!")

                    else:
                        print("Opção de pagamento inválida!")
        else:
            print("Os dados não se coincidem.")
            return matricula_escola()
    
    elif inicial == '2':
        nome_ = str(input("Coloque o seu nome: "))
        cpf_ = str(input("CPF: "))
        cpf_confirm = str(input("Confirme o CPF: "))
        nome_mae = str(input("Nome da mãe: "))
        nome_pai = str(input("Nome do pai: "))
        first_parcela = input("A primeira parcela é de R$500 e assim irá ficar até o final do curso.\nOPÇÕES DE PAGAMENTO:\n[c] - Cartão de crédito\n[d] - Cartão de débito\n[p] - Pix\n[b] - Boleto: ")

        if cpf_ != cpf_confirm:
            print("CPF não confirmado. Pagamento não realizado.")
        else:
            if first_parcela == 'c':
                cartao_credito = input("Digite o número do cartão de crédito: ")
                validade = input("Digite a validade do cartão (MM/AA): ")
                codigo_seguranca = input("Digite o código de segurança do cartão: ")
                print("Pagamento com cartão de crédito realizado com sucesso!")
            elif first_parcela == 'd':
                cartao_debito = input("Digite o número do cartão de débito: ")
                senha = input("Digite a senha do cartão: ")
                print("Pagamento com cartão de débito realizado com sucesso!")
            elif first_parcela == 'p':
                chave_pix = input("Digite a chave PIX: ")
                valor = print("Valor da transação: R$500")
                print("Pagamento com PIX realizado com sucesso!")
            elif first_parcela == 'b':
                boleto = input("Digite o código de barras do boleto: ")
                print("Pagamento com boleto realizado com sucesso!")
            else:
                print("Opção de pagamento inválida!") 
                return matricula_escola()
matricula_escola()


