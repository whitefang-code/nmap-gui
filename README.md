Dependências:
Nmap: O Nmap deve estar instalado no sistema. Ele pode ser instalado via gerenciadores de pacotes como apt (em distribuições Linux baseadas em Debian) ou brew (em macOS).

sudo apt-get install nmap  # Para distribuições baseadas em Debian
brew install nmap          # Para macOS usando Homebrew



Tkinter: Certifique-se de que a biblioteca Tkinter esteja instalada em sua versão do Python:

sudo apt-get install python3-tk

Requisitos do Sistema
Certifique-se de que o Nmap esteja instalado na máquina de destino, já que o seu aplicativo depende do Nmap para funcionar.
Se você tiver um arquivo requirements.txt contendo outras dependências do projeto, pode instalá-las antes de executar o PyInstaller com o comando:
bash

pip install -r requirements.txt

Para o script funcionar é necessário entrar como root. Pode ser o sudo.

sudo python3 main.py

