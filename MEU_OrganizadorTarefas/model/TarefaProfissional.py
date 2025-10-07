from datetime import datetime
from .Tarefa import Tarefa

class TarefaProfissional(Tarefa):
    def __init__(self, nome_tarefa, projeto, data_entrega, descricao=None, data_realizacao=None):
        super().__init__(nome_tarefa, descricao, data_realizacao)
        self.__projeto = projeto
        if isinstance(data_entrega, str):
            try:
                self.__data_entrega = datetime.strptime(data_entrega, "%d-%m-%Y")
            except ValueError as e:
                print(f"[Tarefa Profissional] Data de Entrega em formato inválido: {e}")
                self.__data_entrega = None
        else:
            self.__data_entrega = data_entrega

    def __str__(self):
        return f"[Tarefa Profissional] {super().__str__()}"
    
    @property
    def projeto(self):
        return self.__projeto
    
    @projeto.setter
    def projeto(self, novo_projeto):
        self.__projeto = novo_projeto


    @property
    def data_entrega(self):
        return self.__data_entrega

    @data_entrega.setter
    def data_entrega(self, data):
        if data is not None:
            if isinstance(data, str):
                try:
                    self.__data_entrega = datetime.strptime(data, "%d-%m-%Y")
                except ValueError as e:
                    print(f"[Tarefa Profissional] Data de Entrega em formato inválido: {e}")
                    self.__data_entrega = None
            elif isinstance(data, datetime):
                self.__data_entrega = data
            else:
                print("[Tarefa Profissional] Tipo de data_entrega inválido.")
                self.__data_entrega = None
        else:
            self.__data_entrega = None
        
    
    def exibir_dados(self):
        dados = super().exibir_dados()
        dados = dados.replace("Tarefa cadastrada:", "Tarefa Profissional cadastrada:")
        
        if self.projeto is not None:
            dados += f"  Projeto: {self.projeto}\n" 
        if self.data_entrega is not None:
            data_formatada = self.data_entrega.strftime("%d-%m-%Y")
            dados += f"  Data de entrega: {data_formatada}\n"
        return dados