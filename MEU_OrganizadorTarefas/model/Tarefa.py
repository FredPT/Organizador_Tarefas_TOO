from datetime import datetime

class Tarefa:
    def __init__(self, nome_tarefa, descricao=None, data_realizacao=None):
        self.nome = nome_tarefa
        self.__concluida = False
        self.__descricao = descricao
        self.data_realizacao = data_realizacao

    def concluir(self):
        self.__concluida = True
    
    def exibir_dados(self):
        status = "CONCLUIDO" if self.__concluida else "A FAZER"
        dados = f"Tarefa cadastrada:\n"
        dados += f"  Título: {self.nome} [{status}]\n"
        
        if self.data_realizacao is not None:
            data_formatada = self.data_realizacao.strftime("%d-%m-%Y") 
            dados += f"  Data Prevista: {data_formatada}\n"
        if self.descricao is not None:
            dados += f"  Descrição: {self.descricao}\n"
        return dados

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome


    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, nova_descricao):
        self.__descricao = nova_descricao
    

    @property
    def data_realizacao(self):
        return self.__data_realizacao
    
    @data_realizacao.setter
    def data_realizacao(self, data):
        if data is not None:
            try:
                self.__data_realizacao = datetime.strptime(data, "%d-%m-%Y")
            except ValueError as e:
                print(f"Data em formato inválido: {e}")
        else:
            self.__data_realizacao = None

    def __str__(self):
        status = "Concluída" if self.__concluida == True else "Pendente"
        return f"Tarefa Cadastrada: {self.nome} - {status} - Descrição: {self.__descricao} - Data de Realização: {self.__data_realizacao}"
    

    def __eq__(self, outra_tarefa):
        if(self.nome == outra_tarefa.nome and self.data_realizacao == outra_tarefa.data_realizacao):
            return True
        else:
            return False