from datetime import datetime
from .Tarefa import Tarefa
from .Agendamento import Agendamento

class Compromisso(Tarefa, Agendamento):
    def __init__(self, tarefa: Tarefa, agendamento: Agendamento):
        data_realizacao = tarefa.data_realizacao
        if isinstance(data_realizacao, datetime):
            data_realizacao_str = data_realizacao.strftime("%d-%m-%Y")
        else:
            data_realizacao_str = data_realizacao
            
        Tarefa.__init__(self, tarefa.nome, tarefa.descricao, data_realizacao_str)
        Agendamento.__init__(self, agendamento.nome_agendamento, agendamento._Agendamento__data_inicio, agendamento._Agendamento__data_final, agendamento.atividades, agendamento.local)

        
    def __str__(self):
        return f"[Compromisso]\n{Tarefa.__str__(self)}\n{Agendamento.__str__(self)}"

            
    
    def exibir_dados(self):
        dados = "Compromisso cadastrado:\n"
        dados += Tarefa.exibir_dados(self)
        dados += Agendamento.exibir_dados(self)
        return dados