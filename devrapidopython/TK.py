import tkinter
import webbrowser
from tkinter import messagebox as mb
from tkinter import ttk

def callback(url):
   webbrowser.open_new_tab(url)
def funcExemplo():
    print("Exemplo de funcao")
root = tkinter.Tk()
root.title("SAVA")
root.resizable(False, False)

label = tkinter.Label(root, text="\n")
label.pack()
label = tkinter.Label(root, text="SIA - Sistema de Informações Acadêmicas")
label.pack()
label = tkinter.Label(root, text="Terça, 26 de março de 2024")
label.pack()


test = tkinter.Button(root, text="Entrar com e-mail de estudante")
test['command'] = lambda: test.configure(text="[%s]" % test['text'])
test.pack()

label = tkinter.Label(root, text="\nou\n")
label.pack()

label = tkinter.Label(root, text="Matrícula")
label.pack()
textoEntrada = tkinter.StringVar()
e1 = tkinter.Entry(root)
e1.pack()
link = tkinter.Label(root, text="Não sei ou esqueci a matrícula", fg="blue", cursor="hand2")
link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://example.com/?forget_password"))
link.pack()

label = tkinter.Label(root, text="Senha")
label.pack()
textoEntrada = tkinter.StringVar()
e1 = tkinter.Entry(root, show="*")
e1.pack()
link = tkinter.Label(root, text="Esqueci minha senha / Cadastrar primeira senha", fg="blue", cursor="hand2")
link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://example.com/?forget_password"))
link.pack()

label = tkinter.Label(root, text="\n\n")
label.pack()

test = tkinter.Button(root, text="Entrar")
test.pack()

label = tkinter.Label(root, text="\n")
label.pack()

root.iconify() #Minimiza a tela
root.update()
root.deiconify() #Maximiza a tela
root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs
