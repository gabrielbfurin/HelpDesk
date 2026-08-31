from utils.limpar_terminal import limpar_terminal

def listar_chamados(chamados):
    limpar_terminal()
    if not chamados:
        print("Nenhum chamado registrado.")
        return

    print("\nLista de Chamados:")
    for chamado in chamados:
        chamado.exibir_resumo()