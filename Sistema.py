# 1 - Pessoa fisica / 2 - Pessoa juridica / 3 - Sair
# 1 - Cadastrar Pessoa fisica / 2 - Listar pessoa fisica / 3 - Sair
# 1 - Cadastrar Pessoa juridica / 2 - Listar pessoa juridica / 3 - Sair

from datetime import date, datetime
from Pessoa import Endereco, PessoaFisica


def main():

    lista_pf = []

    while True:
        opcao = int(input('Escolha uma opcao: 1 - Pessoa fisica / 2 - pessoa juricia / 0 - Sair'))

        if opcao == 1:
            while True:
                opcao_pf = int(input('Escolha uma opcao: 1 - Pessoa fisica / 2 - listar pessoa juricia / 0 - voltar ao menu anterior'))

                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()


                    novapf.nome = input('Digite o nome da pessoa fisica')
                    novapf.cpf = input('Digite o CPF')
                    novapf.rendimento = float(input('Digite o rendimento mensal (Digite somente numeros):'))

                    data_nascimento = input('Digite a data de nascimento (DD/MM/aaa): ')
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365


                    if idade >= 18:
                        print('A pessoa tem mais de 18 anos')
                    else:
                        print('A pessoa tem menod de 18 anos. Retorne ao menu..')
                        continue 

                    novo_end_pf.logradouro = input('Digite o logradouro: ')
                    novo_end_pf.numero = input('Digite o numero: ')
                    end_comerical = input('Este endeco e comercial? S/N?')
                    novo_end_pf.endereco_Comercial = end_comerical.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print('Cadastro realizado')

                #LISTAR PESSOA FISICA
                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f'Nome: {cada_pf.nome}')
                            print(f'CPF: {cada_pf.cpf}')
                            print(f'Endereco: {cada_pf.endereco.logradouro}, { cada_pf.endereco.numero}')
                            print(f'Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}')
                            print(f'Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}')
                            print('Digite 0 para sair')
                            print()

                    else:
                        print('Lista Vazia')

                # SAIR DO MENU ATUAL
                elif opcao_pf == 0:
                    print('Voltando ao menu anterior')
                    break

                else:
                    print('Opcao invalida, por favor digite uma das opcoes indicadas:')

        elif opcao == 2:
             print('Funcionalidade para pessoa juridica nao implementada')

        elif opcao == 0:
            print('Obrigada por ultilizar o sistema')
            break

        else:
            print('Opcao invalida, digite uma opcao valida')

if __name__ == '__main__':
    main()


        





            

            
            
            
            
                


