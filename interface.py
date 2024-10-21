import tkinter as tk
from tkinter import messagebox, ttk

class NmapInterface:
    def __init__(self, janela, executar_nmap):
        self.janela = janela
        self.executar_nmap = executar_nmap
        self.configurar_janela()

    def configurar_janela(self):
        self.janela.title("Nmap Frontend")
        self.janela.geometry("600x750")
        
        # Configura a grade para redimensionar
        for i in range(13):  # Para o número de linhas que temos
            self.janela.grid_rowconfigure(i, weight=1)
        self.janela.grid_columnconfigure(1, weight=1)  # Permite que a coluna 1 se expanda

        # Entrada para o alvo
        self.label_alvo = tk.Label(self.janela, text="Alvo:")
        self.label_alvo.grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.entry_alvo = tk.Entry(self.janela, width=50)
        self.entry_alvo.grid(row=0, column=1, padx=10, pady=5)

        # Combobox para as opções de varredura
        self.label_varredura = tk.Label(self.janela, text="Tipo de varredura:")
        self.label_varredura.grid(row=1, column=0, sticky='w', padx=10, pady=5)

        self.opcoes_varredura = [
            "-sS (SYN Scan)",
            "-sT (TCP Connect Scan)",
            "-sU (UDP Scan)",
            "-sP (Ping Scan)",
            "-sV (Versão do serviço)",
            "-O (Detecção de SO)",
            "-A (Detecção agressiva)",
            "--traceroute (Rastrear rota)",
            "-Pn (Desabilitar ping)",
        ]

        self.combobox_varredura = ttk.Combobox(self.janela, values=self.opcoes_varredura)
        self.combobox_varredura.grid(row=1, column=1, padx=10, pady=5)
        self.combobox_varredura.current(0)

        # Verbosidade
        self.label_verbosidade = tk.Label(self.janela, text="Verbosidade:")
        self.label_verbosidade.grid(row=2, column=0, sticky='w', padx=10, pady=5)

        self.opcoes_verbosidade = [
            "Nenhuma",
            "-v (Verbosidade 1)",
            "-vv (Verbosidade 2)",
            "-d (Depuração 1)",
            "-dd (Depuração 2)",
        ]

        self.combobox_verbosidade = ttk.Combobox(self.janela, values=self.opcoes_verbosidade)
        self.combobox_verbosidade.grid(row=2, column=1, padx=10, pady=5)
        self.combobox_verbosidade.current(0)

        # Opções de saída
        self.label_saida = tk.Label(self.janela, text="Opções de Saída:")
        self.label_saida.grid(row=3, column=0, sticky='w', padx=10, pady=5)

        self.var_saida_normal = tk.BooleanVar()
        self.checkbox_saida_normal = tk.Checkbutton(self.janela, text="Saída Normal (-oN)", variable=self.var_saida_normal)
        self.checkbox_saida_normal.grid(row=4, column=0, sticky='w', padx=10)

        self.var_saida_xml = tk.BooleanVar()
        self.checkbox_saida_xml = tk.Checkbutton(self.janela, text="Saída XML (-oX)", variable=self.var_saida_xml)
        self.checkbox_saida_xml.grid(row=5, column=0, sticky='w', padx=10)

        self.var_saida_grep = tk.BooleanVar()
        self.checkbox_saida_grep = tk.Checkbutton(self.janela, text="Saída Grepable (-oG)", variable=self.var_saida_grep)
        self.checkbox_saida_grep.grid(row=6, column=0, sticky='w', padx=10)

        self.var_saida_script = tk.BooleanVar()
        self.checkbox_saida_script = tk.Checkbutton(self.janela, text="Saída Script Kiddie (-oS)", variable=self.var_saida_script)
        self.checkbox_saida_script.grid(row=7, column=0, sticky='w', padx=10)

        # Seleção de scripts de vulnerabilidade
        self.label_scripts = tk.Label(self.janela, text="Scripts NSE:")
        self.label_scripts.grid(row=8, column=0, sticky='w', padx=10, pady=5)

        self.opcoes_scripts = [
            "Nenhum",
            "vuln (Todos os scripts de vulnerabilidade)",
            "ftp-vsftpd-backdoor",
            "http-heartbleed",
            "smb-vuln-ms17-010",
            "ssl-poodle",
            "dns-zone-transfer",
            # Adicione mais scripts conforme necessário
        ]

        self.combobox_scripts = ttk.Combobox(self.janela, values=self.opcoes_scripts)
        self.combobox_scripts.grid(row=8, column=1, padx=10, pady=5)
        self.combobox_scripts.current(0)

        # Entrada para o intervalo de portas
        self.label_portas = tk.Label(self.janela, text="Intervalo de Portas (Opcional):")
        self.label_portas.grid(row=9, column=0, sticky='w', padx=10, pady=5)

        self.frame_portas = tk.Frame(self.janela)
        self.frame_portas.grid(row=10, columnspan=2, padx=10, pady=5)

        self.label_porta_inicial = tk.Label(self.frame_portas, text="Porta Inicial:")
        self.label_porta_inicial.grid(row=0, column=0, padx=5)
        self.entry_porta_inicial = tk.Entry(self.frame_portas, width=10)
        self.entry_porta_inicial.grid(row=0, column=1, padx=5)

        self.label_porta_final = tk.Label(self.frame_portas, text="Porta Final:")
        self.label_porta_final.grid(row=0, column=2, padx=5)
        self.entry_porta_final = tk.Entry(self.frame_portas, width=10)
        self.entry_porta_final.grid(row=0, column=3, padx=5)

        # Botão para executar o Nmap
        self.botao_executar = tk.Button(self.janela, text="Executar Nmap", command=self.executar_nmap_handler)
        self.botao_executar.grid(row=11, columnspan=2, pady=10)

        # Área de texto para exibir o resultado
        self.text_resultado = tk.Text(self.janela, wrap="word", height=20)
        self.text_resultado.grid(row=12, columnspan=2, padx=10, pady=5)

    def obter_dados(self):
        return {
            "alvo": self.entry_alvo.get(),
            "varredura": self.combobox_varredura.get(),
            "verbosidade": self.combobox_verbosidade.get(),
            "porta_inicial": self.entry_porta_inicial.get(),
            "porta_final": self.entry_porta_final.get(),
            "saida_normal": self.var_saida_normal.get(),
            "saida_xml": self.var_saida_xml.get(),
            "saida_grep": self.var_saida_grep.get(),
            "saida_script": self.var_saida_script.get(),
            "script_vulnerabilidade": self.combobox_scripts.get(),
        }

    def executar_nmap_handler(self):
        """Lida com o clique no botão de executar Nmap."""
        dados = self.obter_dados()
        if not dados["alvo"]:
            messagebox.showwarning("Aviso", "Por favor, insira um alvo.")
            return
        self.text_resultado.delete(1.0, tk.END)  # Limpa a área de texto
        self.executar_nmap(dados)

    def exibir_saida(self, saida):
        """Exibe a saída do Nmap na área de texto."""
        self.text_resultado.insert(tk.END, saida + "\n")
        self.text_resultado.see(tk.END)  # Rola para baixo

