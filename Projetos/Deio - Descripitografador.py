from cryptography.fernet import Fernet
import os

# Montando um Script para descriptografar com chave

def carregar_chave():
    return open("chave.key", 'rb').read()

def descriptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo,'rb') as file:
        dados = file.read()
        dados_descripitogrfados = f.decrypt(dados)
    with open(arquivo, 'wb') as file:
        file.write(dados_descripitogrfados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos('test_file')
    for arquivo in arquivo:
        descriptografar_arquivo(arquivo, chave)
    print('Arquivos descriptografados')