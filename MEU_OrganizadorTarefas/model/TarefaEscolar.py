from datetime import datetime
from .Tarefa import Tarefa

class TarefaEscolar(Tarefa):
    def __init__(self, nome_tarefa, disciplina, peso=0, descricao=None, data_realizacao=None, data_entrega=None):
        super().__init__(nome_tarefa, descricao, data_realizacao)
        self.__disciplina = disciplina
        self.__peso = peso
        self.data_entrega = data_entrega

    def __str__(self):
        return f"[Tarefa Escolar] {super().__str__()}"
    

    @property
    def disciplina(self):
        return self.__disciplina
    
    @disciplina.setter
    def disciplina(self, nova_disciplina):
        self.__disciplina = nova_disciplina
        

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, novo_peso):
        self.__peso = novo_peso
        
    @property
    def data_entrega(self):
        return self.__data_entrega

    @data_entrega.setter
    def data_entrega(self, data):
        if data is not None:
            try:
                self.__data_entrega = datetime.strptime(data, "%d-%m-%Y")
            except ValueError as e:
                print(f"[TarefaEscolar] Data de Entrega em formato inválido: {e}")
                self.__data_entrega = None
        else:
            self.__data_entrega = None
        
    
    def exibir_dados(self):
        dados = super().exibir_dados()
        
        dados = dados.replace("Tarefa cadastrada:", "Tarefa Escolar cadastrada:")
        
        if self.disciplina is not None:
            dados += f"  Disciplina: {str(self.disciplina)}\n" 
        if self.peso != 0:
            dados += f"  Peso: {float(self.peso)}\n"
        if self.data_entrega is not None:
            data_formatada = self.data_entrega.strftime("%d-%m-%Y")
            dados += f"  Data de entrega: {data_formatada}\n"
        return dados