import tkinter as tk
from tkinter import messagebox

def gerar_tabuada():
    try:
        numero = int(entrada.get())
        resultado.delete('1.0', tk.END)
        for i in range(1, 11):
            resultado.insert(tk.END, f"{numero} x {i} = {numero*i}\n")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido.")

def sair():
    janela.destroy()

# Janela principal
janela = tk.Tk()
janela.title("Tabuada Interativa")
janela.geometry("300x450")

# Entrada de número
tk.Label(janela, text="Digite um número:").pack(pady=10)
entrada = tk.Entry(janela)
entrada.pack()

# Botão de gerar tabuada
tk.Button(janela, text="Gerar Tabuada", command=gerar_tabuada).pack(pady=10)

# Área de resultado
resultado = tk.Text(janela, height=10, width=30)
resultado.pack()

# Botão de sair
tk.Button(janela, text="Sair", command=sair).pack(pady=10)

# Créditos do desenvolvedor
tk.Label(janela, text="Desenvolvido por Luis Orlando", font=("Arial", 10), fg="gray").pack(side="bottom", pady=5)

# Loop da interface
janela.mainloop()
