from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar
from model.Disciplina import Disciplina

"""
t1 = Tarefa("Aula de TOO", "Estudar os conceitos de POO")
print(t1.exibir_dados())
t1.concluir()
print(t1.exibir_dados())

t2 = Tarefa("Estudar Python", "Estudar os conceitos de Python", "18-09-2025")
print(t2.data_realizacao)
t2.data_realizacao = "17-09-2025"
print(t2.data_realizacao)
print(t2.exibir_dados())

t3 = Tarefa("Estudar Python", "Estudar os conceitos de Python", "15-02-2025")
t4 = Tarefa("Estudar Python", "Estudar os conceitos de Python", "15-02-2025")

if(t3 == t4):
    print("São iguais")
else:
    print("São diferentes")

t5 = TarefaEscolar("Introdução Herança", "TOO")
print(t5.exibir_dados())
t5.peso = 2
t5.descricao = "Estudar os conceitos de Herança"
t5.data_entrega = "20-09-2025"
print(t5.exibir_dados())
"""


"""
# Testando a classe Disciplina aula 24/09

disciplina_too = Disciplina("Tecnologia de Orientação à Objetos", "Curso BCC", 80, "Prof Vanessa")
disciplina_poo = Disciplina("Programação Orientada à Objetos", "Curso BCC", 60, "Prof Vanessa")
disciplina_bd = Disciplina("Banco de Dados", "Curso BCC", 80, "Prof Bertei")


# Testar o str de Discilina
print("\n\nDisciplinas Criadas")
print(str(disciplina_too))
print(str(disciplina_poo))
print(str(disciplina_bd))
print("\n")
print(disciplina_too.exibir_dados())
print("\n")


t1 = Tarefa("Fazer exercício físico", "Corrida", "25-09-2025")
tarefa_escolar_1 = TarefaEscolar("Introdução à Herança", disciplina_too, 2, data_realizacao="24-09-2025", data_entrega="30-09-2025")
tarefa_escolar_2 = TarefaEscolar("Modelagem de Dados", disciplina_bd, 1, descricao="Criar o diagrama lógico do projeto", data_realizacao="24-09-2025", data_entrega="15-10-2025")

# Tarefa genérica
print("\n")
print(t1.exibir_dados())

# Tarefa escolar 1
print(tarefa_escolar_1.exibir_dados())

# Tarefa escolar 2
print(tarefa_escolar_2.exibir_dados())
"""

# 01/10/2025 Criando Agendamento, TarefaProfissional/Pessoal e Compromisso
from model.TarefaProfissional import TarefaProfissional
from model.TarefaPessoal import TarefaPessoal
from model.Agendamento import Agendamento
from model.Compromisso import Compromisso

tarefa = Tarefa("Reunião de Projeto", "Discutir requisitos", "01-10-2025")
agendamento = Agendamento("Reunião de Arena Games", "2025-10-10 14:00", "2025-10-10 15:00", "Apresentação, Discussão", "Sala 502")

compromisso = Compromisso(tarefa, agendamento)
print(compromisso.exibir_dados())