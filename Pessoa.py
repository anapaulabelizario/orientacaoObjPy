#CLASSE ENDERECO
from datetime import date


class Endereco:
    def _init_(self, logradouro="", numero="", endereco_Comercial=False):
        # Inicializar os nossos atributos com valores padrao
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial#CLASSE PESSOA

class Pessoa:
    def _init_(self, nome="", rendimento=0.0, endereco=None) :
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco
        

    def calcular_imposto(self, rendimento):
        return rendimento

#CLASSE PESSOA FISICA
    #Inicializar os atributos que foram herdados e os proprios atributos da classe
class PessoaFisica(Pessoa):
    def _init_ (self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        if endereco is None:
            # Se nenhum endereco for fornecido, cria um objeto de endereco padrao
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()

            super()._init_(nome, rendimento, endereco) 
            #Chama o construtor da superclasse Pessoa para inicializar os atributos herdados


        #Atributos da propria classe
        self.cpf = cpf
        self.dataNascimento = dataNascimento

    def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimento entre 1500 e 3500
        if rendimento <= 1500:
            return 0
        #2% de imposto para rendimento entre 1500 e 3500
        elif 1500 < rendimento <= 3500:
            return(rendimento / 100) * 2
        #3.5% de imposto para rendimentos entre 3500 e 6000
        elif 3000 < rendimento <= 6000:
            return (rendimento/ 100) * 3.5
        #5% de impostos para rendimentos acima de 6000
        else:
            return rendimento * 5

#CLASSE PESSOA JURIDICA

class PessoaJuridica(Pessoa):
    def _init_(self, nome="", rendimento=0, cnpj="", endereco=None, dataFundacao=None):
        
        if endereco is None:
            # Se nenhum endereco for fornecido, cria um objeto de endereco padrao
            endereco = Endereco()

            super()._init_(nome, rendimento, endereco) 
            #Chama o construtor da superclasse Pessoa para inicializar os atributos herdados

        #Atributos da propria classe
        self.cnpj = cnpj
        self.dataFundacao = dataFundacao

    def calcular_imposto(self, rendimento: float) -> float:
        # Sem imposto para rendimento entre 10000 e 100000
        if rendimento <= 10000:
            return 0
        #2% de imposto para rendimento entre 10000 e 100000
        elif 10000 < rendimento <= 100000:
            return(rendimento / 100) * 2
        #3.5% de imposto para rendimentos entre 100000 e 500000
        elif 100000 < rendimento <= 500000:
            return (rendimento/ 100) * 3.5
        #5% de impostos para rendimentos acima de 500000
        else:
            return rendimento * 5


