# 1 - Pessoa Fisica / 2 - Pessoa Juridica /3 - Sair
# 1 - Cadastrar Pessoa Fisica / 2- Listar Pessoa Física / 3 - Sair
# 1 - Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Sair

from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica, PessoaJuridica


def main():
    lista_pf = []
    lista_pj = []
    while True:
        opcao = int(input('Escolha uma opcao: 1 - Pessoa Física / 2 - Pessoa Jurídica / 0 - Sair'))

        if opcao == 1:
            while True:
                opcao_pf = int(input('Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Voltar ao menu anterior / 0 - Remover CPF da lista'))

                #1 Cadastrar uma Pessoa Fisica
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input('Digite o nome da pessoa física: ')
                    novapf.cpf = input('Digite o CPF: ')
                    novapf.rendimento = float(input('Digite o rendimento mensal (Digite somente números): '))
                    

                    data_nascimento = input('Digite a data de Nascimento (dd/MM/aaaa): ') #Solicita a data de nascimento
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365 #Calcula idade da pessoa

                    if idade >= 18:
                        print('A pessoa tem mais de 18 anos')
                    else:
                        print('A pessoa tem menos de 18 anos. Retorne ao menu...')
                        continue #Retornar ao inicio do loop

                    #CADASTRO DE ENDERECO
                    novo_end_pf.logradouro = input('Digite o logradouro: ')
                    novo_end_pf.numero = input('Digite o número: ')
                    end_comercial = input ('Este endereco é comercial: S/N: ') #Solicitar se o endereco é comercial
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S' 

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)



                    print('Cadastro realizado com sucesso!!')
                #LISTAR PESSOA FISICA
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f'Nome: {cada_pf.nome}')
                            print(f'CPF: {cada_pf.cpf}')
                            print(f'Endereco: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}')
                            print(f'Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}')
                            print(f'Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}')
                            print('Digite 0 para sair')
                            
                            input()
                    else:
                        print('Lista Vazia')
                    #REMOVER PESSOA
                elif opcao_pf == 0:
                    cpf_para_remover = input('Digite o CPF da pessoa física que deseja remover: ')

                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_remover:
                            lista_pf.remove(cada_pf)
                            pessoa_encontrada = True
                            print('Pessoa fisica removida! ')

                            break
                    if not pessoa_encontrada :
                         print('Nenhuma pessoa encontrada! ')

                elif opcao_pf ==4:
                    cpf_para_atualizar = input('Digite o CPF que deseja atualizar: ')
                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_atualizar:
                            pessoa_encontrada = True

                            print('Escola qual dado deseja atualizar')
                            print('N - Nome')
                            print('R - Rendimento')
                            print('L - Logradouro')
                            print('N - Numero do endereco')

                            escolha = input('Digite a inicial do atributo')

                            if escolha == 'N':
                                novo_nome = input(f'O nome atual e {cada_pf.nome}. Digite o novo nome:')
                                cada_pf.nome = novo_nome

                            elif escolha == 'R':
                                novo_rendimento = input(f'O rendimento atual e {cada_pf.rendimento}. Digite o novo rendimento:')
                                cada_pf.rendimento = novo_rendimento

                            elif escolha == 'L':
                                novo_logradouro = input(f'O logradouro atual e {cada_pf.logradouro}. Digite o novo logradouro:')
                                cada_pf.logradouro = novo_logradouro

                            elif escolha == 'N':
                                novo_numero = input(f'O numero atual e {cada_pf.numero}. Digite o novo numero:')
                                cada_pf.numero = novo_numero

                            else:
                                print('Opcao invalida')
                                break

                    if not pessoa_encontrada:
                        print('Nenhuma pessoa com esse CPF foi encontrada')





     


            
                #SAIA DO MENU ATUAL
                elif opcao_pf == 0:
                    print('Voltando ao menu anterior')
                    break

                else:
                    print('Opcao invalida, por favor digite uma das opcoes indicadas: ')
        #CADASTRAR PESSOA JURIDICA
        elif opcao == 2:
            novapj = PessoaJuridica()
            novo_end_pj = Endereco()

            novapj.nome = input('Digite o nome da pessoa juridica: ')
            novapj.cnpj = input('Digite o CNPJ: ')
            novapj.rendimento = float(input('Digite o rendimento mensal (Digite somente números): '))

            
            data_fundacao = input('Digite a data de fundacao (dd/MM/aaaa): ') #Solicita a data de fundacao
            novapj.dataFundacao = datetime.strptime(data_fundacao, '%d/%m/%Y').date()
            tempo_empresa = (date.today() - novapj.dataFundacao).days // 365 #Calcula tempo da empresa


            if tempo_empresa > 10:
                print('Esta empresa já tem mais de 10 anos')
            else:
                print('A empresa tem menos de 10 anos. Retorne ao menu...')
                continue #Retornar ao inicio do loop



            #CADASTRO DE ENDERECO
            novo_end_pj.logradouro = input('Digite o logradouro: ')
            novo_end_pj.numero = input('Digite o número: ')
            end_comercial = input ('Este endereco é comercial: S/N: ') #Solicitar se o endereco é comercial
            novo_end_pj.endereco_Comercial = end_comercial.strip().upper() == 'S' 

            novapj.endereco = novo_end_pj

            lista_pj.append(novapj)

            print('Cadastro realizado com sucesso!!')
    
        elif opcao == 0:
            print('Obrigada por utilizar o nosso sistema! Valeu!')
            break

        else:
            print('Opcao invalida, por favor digite uma das opcoes válidas')
    
if _name_ == '_main_':
    main() #Chama funcao principal


        





            

            
            
            
            
                


