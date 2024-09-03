import tkinter
import webbrowser
from tkinter import messagebox as mb
from tkinter import ttk
from PIL import Image, ImageTk

def callback(url):
   webbrowser.open_new_tab(url)

def funclogin():
    login = str(EntradaLogin.get())
    senha = str(EntradaSenha.get())
    if login == str("admin") and senha == str("admin"):
        tela2()
    else:
        mb.showerror("Erro", "Login e senha incorretos.")


def limpartela():
    for tirar in root.winfo_children():
        tirar.destroy()

def tela2():
    limpartela()
    root.geometry("800x700")
    bg = Image.open("bg.png")
    bgtest = ImageTk.PhotoImage(bg)
    label = tkinter.Label(image=bgtest)
    label.image = bgtest
    label.place(x=0, y=0)
    i1 = Image.open("img1.png")
    imagem1 = ImageTk.PhotoImage(i1)
    label1 = tkinter.Label(image=imagem1)
    label1.image = imagem1
    label1.grid(row=0,column=0)
    i2 = Image.open("img2.png")
    imagem2 = ImageTk.PhotoImage(i2)
    label2 = tkinter.Label(image=imagem2)
    label2.image = imagem2
    label2.grid(row=1,column=1)
    botao1 = tkinter.Button(root, text="gato",command=lambda: mb.showerror("Erro", "Isso não é um gato."))
    botao1.grid(row=0, column=1)


root = tkinter.Tk()
root.geometry("200x300")
root.title("Login")
root.resizable(False, False)

bg = Image.open("bg.png")
bgtest = ImageTk.PhotoImage(bg)
labelbg = tkinter.Label(image=bgtest)
labelbg.image = bgtest
labelbg.place(x=0, y=0)


label = tkinter.Label(root, text="\n\n")
label.pack()

label = tkinter.Label(root, text="  Login", anchor="w")
label.pack(fill='both')
EntradaLogin = tkinter.Entry(root, width=30)
EntradaLogin.pack()
link = tkinter.Label(root, text="Esqueci o login", fg="blue", cursor="hand2", anchor="e", font=("Segoe UI", 7))
link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.youtube.com/watch?v=L8XbI9aJOXk"))
link.pack(fill='both')

label = tkinter.Label(root, text="  Senha", anchor="w")
label.pack(fill='both')
EntradaSenha = tkinter.Entry(root, show="*", width=30)
EntradaSenha.pack()
link = tkinter.Label(root, text="Esqueci minha senha", fg="blue", cursor="hand2", anchor="e", font=("Segoe UI", 7))
link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://www.youtube.com/watch?v=L8XbI9aJOXk"))
link.pack(fill='both')

label = tkinter.Label(root, text="\n\n")
label.pack()

botaologin = tkinter.Button(root, text="Entrar",command=lambda: funclogin())
botaologin.pack()

label = tkinter.Label(root, text="\n")
label.pack()

root.iconify() #Minimiza a tela
root.update()
root.deiconify() #Maximiza a tela
root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs