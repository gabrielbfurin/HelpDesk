import models.chamado as Chamado
from services.listar_chamados import listar_chamados
from utils.limpar_terminal import limpar_terminal

def criar_chamado():
    print("Help Desk - Sistema de Chamados")
    nome_solicitante = input("Nome do solicitante: ")
    departamento = input("Departamento: ")
    titulo = input("Título do chamado: ")
    descricao = input("Descrição do chamado: ")
    prioridade = input("Prioridade (Baixa, Média, Alta): ")

    chamado = Chamado.Chamado(nome_solicitante, departamento, titulo, descricao, prioridade)
    chamado.exibir_resumo()
    return chamado

def main():
    limpar_terminal()
    chamados = []

    chamados.append(criar_chamado())
    chamados.append(criar_chamado())

    listar_chamados(chamados)

if __name__ == "__main__":
    main()