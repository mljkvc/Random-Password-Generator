import tkinter as tk
import random as rn
import string
import pyperclip as pc

stop = True

def generisi_loop():
    global stop
    global sifra
    if stop:
        karakteri = string.ascii_letters + string.digits + string.punctuation
        sifra = ''.join(rn.choice(karakteri) for i in range(16))
        label.config(text = sifra)
        label.after(69, generisi_loop)
    else:
        print(f"Your new password: {sifra} is coppied to clipboard")
        pc.copy(sifra)

def stisnut():
    global stop
    if stop:
        button.config(text = "Rerun")
        stop = False
        return
    
    stop = True
    button.config(text = "Stop")
    generisi_loop()


window = tk.Tk()
window.title("Password generator")
window.geometry("400x100")
window.configure(bg = "Black")

label = tk.Label(window, text = "sifra")
label.configure(bg = "Black", fg = "Green")
label.config(font = ("MobileFont", 20))
label.configure(width = 20)

button = tk.Button(window, text = "Stop", command = stisnut)
button.configure(bg = "Black", fg = "Green")
button.config(font = ("MobileFont", 20))

label.pack()
button.pack()

generisi_loop()
window.mainloop()