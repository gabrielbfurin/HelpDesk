from services.gerar_id import gerar_id

class Chamado():
    def __init__(self, nome_solicitante, departamento, titulo, descricao, prioridade):
        self.nome_solicitante = nome_solicitante
        self.departamento = departamento
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = "Aberto"  # Status inicial do chamado
        self.id = gerar_id()  # Gera um ID único para o chamado

    def exibir_resumo(self):
        print("\nResumo do Chamado:")
        print(f"Nome: {self.nome_solicitante}")
        print(f"Departamento: {self.departamento}")
        print(f"Título: {self.titulo}")
        print(f"Descrição: {self.descricao}")
        print(f"Prioridade: {self.prioridade}")
        print(f"Status: {self.status}")
        print(f"ID do Chamado: {self.id}")