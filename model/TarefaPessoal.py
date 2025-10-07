from datetime import datetime
from .Tarefa import Tarefa

class TarefaPessoal(Tarefa):
    def __init__(self, nome_tarefa, tipo, descricao=None, data_realizacao=None):
        super().__init__(nome_tarefa, descricao, data_realizacao)
        self.__tipo = tipo

    def __str__(self):
        return f"[Tarefa Pessoal] {super().__str__()}"
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, novo_tipo):
        self.__tipo = novo_tipo
       
    
    def exibir_dados(self):
        dados = super().exibir_dados()
        dados = dados.replace("Tarefa cadastrada:", "Tarefa Pessoal cadastrada:")
        dados += f"  Tipo: {self.tipo}\n"
        return dados