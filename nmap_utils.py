import os
import subprocess

def verifica_privilegios():
    """Verifica se o script está sendo executado com privilégios de superusuário."""
    if os.geteuid() != 0:
        print("Este script precisa ser executado com privilégios de superusuário. Execute-o como 'sudo'.")
        exit(1)

def construir_comando(dados):
    """Constrói o comando Nmap baseado nos dados fornecidos pela GUI."""
    opcoes = [dados['varredura'].split()[0]]

    # Acrescenta as opções de portas
    if dados['porta_inicial'] or dados['porta_final']:
        porta_inicial = dados['porta_inicial']
        porta_final = dados['porta_final']
        if porta_inicial and not porta_final:
            opcoes.append(f"-p {porta_inicial}")
        elif porta_inicial and porta_final:
            opcoes.append(f"-p {porta_inicial}-{porta_final}")

    # Verbosidade
    if dados["verbosidade"] and dados["verbosidade"] != "Nenhuma":
        opcoes.append(dados["verbosidade"].split()[0])

    # Scripts de vulnerabilidade
    if dados["script_vulnerabilidade"] and dados["script_vulnerabilidade"] != "Nenhum":
        opcoes.append(f"--script {dados['script_vulnerabilidade']}")

    # Opções de saída
    if dados["saida_normal"]:
        opcoes.append("-oN output.txt")
    if dados["saida_xml"]:
        opcoes.append("-oX output.xml")
    if dados["saida_grep"]:
        opcoes.append("-oG output.gnmap")
    if dados["saida_script"]:
        opcoes.append("-oS output.script")

    comando_nmap = " ".join(opcoes)
    return f"nmap {comando_nmap} {dados['alvo']}"

def executar_nmap(dados, callback):
    """Executa o Nmap com os dados fornecidos e chama a função de callback com a saída."""
    comando = construir_comando(dados)

    # Executa o comando e captura a saída
    process = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            callback(output.decode().strip())

    rc = process.poll()
    return rc

