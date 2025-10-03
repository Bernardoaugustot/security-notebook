def Logar():
    entrada = input().strip()  

    # Divide a string em uma lista, removendo espaços e mantendo tudo minúsculo por segurança
    tentativas = [item.strip().lower() for item in entrada.split(',')]

    # Inicializa o contador de falhas consecutivas
    falhas_consecutivas = 0

    # TODO: Percorra cada tentativa da lista:
    for item in tentativas:
        if item =='sucesso': falhas_consecutivas = 0
        if item == "falha": falhas_consecutivas+=1
        if falhas_consecutivas >= 3: return print("Conta Bloqueada")
        
    return print("Acesso Normal")
Logar()