import tkinter as tk
import nmap_utils
from interface import NmapInterface

# Verifica se o script está rodando com privilégios de superusuário
nmap_utils.verifica_privilegios()

def executar_nmap(dados):
    """Função que executa o Nmap e exibe a saída."""
    def callback_saida(saida):
        gui.exibir_saida(saida)

    nmap_utils.executar_nmap(dados, callback_saida)

# Configuração da interface
janela = tk.Tk()
gui = NmapInterface(janela, executar_nmap)
janela.mainloop()

