from model.Tarefa import Tarefa
from model.TarefaEscolar import TarefaEscolar
from model.Disciplina import Disciplina
from model.TarefaProfissional import TarefaProfissional
from model.TarefaPessoal import TarefaPessoal
from model.Agendamento import Agendamento
from model.Compromisso import Compromisso

print("=== Teste Tarefa ===")
tarefa = Tarefa("Estudar Python", "Revisar listas", "08-10-2025")
print(tarefa.exibir_dados())
tarefa.concluir()
print(tarefa.exibir_dados())

print("\n=== Teste Disciplina ===")
disciplina = Disciplina("TOO", "BCC", 60, "Prof. Vanessa")
print(disciplina.exibir_dados())

print("\n=== Teste Tarefa Escolar ===")
tarefa_escolar = TarefaEscolar("Trabalho de TOO", disciplina, 2, descricao="Fazer herança multipla", data_realizacao="01-10-2025", data_entrega="08-10-2025")
print(tarefa_escolar.exibir_dados())

print("\n=== Teste Tarefa Profissional ===")
tarefa_profissional = TarefaProfissional("Relatório Final", "Projeto Migração SAS para PySpark", "12-10-2025", "Preparar relatório", "08-10-2025")
print(tarefa_profissional.exibir_dados())

print("\n=== Teste Tarefa Pessoal ===")
tarefa_pessoal = TarefaPessoal("Caminhada", "Saúde", "Exercício para a noite", "09-10-2025")
print(tarefa_pessoal.exibir_dados())

print("\n=== Teste Agendamento ===")
agendamento = Agendamento("Consulta Médica", "2025-10-10 09:00", "2025-10-10 10:00", "Consulta, Exames", "Clínica Unimed Vera Cruz")
print(agendamento.exibir_dados())

print("\n=== Teste Compromisso ===")
compromisso = Compromisso(tarefa, agendamento)
print(compromisso.exibir_dados())