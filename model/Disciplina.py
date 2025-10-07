class Disciplina:
    def __init__(self, nome, curso, carga_horaria=0, professor=None):
        self.nome = nome
        self.__curso = curso
        if(0 < carga_horaria < 1000):
            self.__carga_horaria = carga_horaria
        else:
            print("Valor para Carga Horária inválido!!")
        self.professor = professor

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.strip()

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso):
        self.__curso = curso.strip()

    def __str__(self):
        return f"{self.nome} ({self.curso})"
    
    def exibir_dados(self):
        dados = f"Disciplina: {self.nome} ({self.curso})\n"
        dados += f"Carga Horária: {self.__carga_horaria}h\n"
        dados += f"Professor: {self.professor}\n"
        return dados