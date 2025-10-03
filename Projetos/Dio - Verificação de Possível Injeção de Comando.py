def verificar_comando(comando):
    # Caracteres suspeitos para injeção de comando
    caracteres_suspeitos = [';', '&', '|', '$']
    
    for char in comando:
        for inspeciona in caracteres_suspeitos:
            if char == inspeciona: 
                return print("Comando Suspeito")   
    return print("Comando Seguro")

# Entrada do usuário
comando_usuario = input()

verificar_comando(comando_usuario)