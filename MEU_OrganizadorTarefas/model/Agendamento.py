from datetime import datetime

class Agendamento:
    def __init__(self, nome_agendamento, data_inicio, data_final, atividades, local):
        self.nome_agendamento = nome_agendamento
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.atividades = atividades
        self.local = local
    
    def __str__(self):
        return f"[Agendamento] {self.nome_agendamento} - {self.__data_inicio} até {self.__data_final}"


    @property
    def data_inicio(self):
        return self.__data_inicio
    
    @data_inicio.setter
    def data_inicio(self, novo_inicio):
        if isinstance(novo_inicio, str):
            try:
                self.__data_inicio = datetime.strptime(novo_inicio, "%Y-%m-%d %H:%M")
            except ValueError:
                try:
                    self.__data_inicio = datetime.strptime(novo_inicio, "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Data de início deve estar no formato 'YYYY-MM-DD' ou 'YYYY-MM-DD HH:MM'")
        elif isinstance(novo_inicio, datetime):
            self.__data_inicio = novo_inicio
        else:
            self.__data_inicio = None

    @property
    def data_final(self):
        return self.__data_final

    @data_final.setter
    def data_final(self, novo_final):
        if isinstance(novo_final, str):
            try:
                self.__data_final = datetime.strptime(novo_final, "%Y-%m-%d %H:%M")
            except ValueError:
                try:
                    self.__data_final = datetime.strptime(novo_final, "%Y-%m-%d")
                except ValueError:
                    raise ValueError("Data final deve estar no formato 'YYYY-MM-DD' ou 'YYYY-MM-DD HH:MM'")
        elif isinstance(novo_final, datetime):
            self.__data_final = novo_final
        else:
            self.__data_final = None

   
    def exibir_dados(self):
        dados = f"\nAgendamento: {self.nome_agendamento}\n"
        dados += f"  Data de Início: {self.data_inicio.strftime('%d/%m/%Y %H:%M')}\n"
        dados += f"  Data Final: {self.data_final.strftime('%d/%m/%Y %H:%M')}\n"
        dados += f"  Atividades: {self.atividades}\n"
        dados += f"  Local: {self.local}\n"
        return dados
    