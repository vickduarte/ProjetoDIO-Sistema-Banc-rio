import tkinter as tk
from tkinter import messagebox

# Funções de operação
def depositar():
    global saldo
    valor = float(entry_valor.get())
    if valor > 0:
        saldo += valor
        atualizar_extrato(f"Depósito: R$ {valor:.2f}")
        atualizar_saldo()
    else:
        messagebox.showerror("Erro", "O valor informado é inválido.")

def sacar():
    global saldo, numero_saques
    valor = float(entry_valor.get())
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        messagebox.showerror("Erro", "Você não tem saldo suficiente.")
    elif excedeu_limite:
        messagebox.showerror("Erro", "O valor diário do saque excede o limite.")
    elif excedeu_saques:
        messagebox.showerror("Erro", "Número máximo de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        atualizar_extrato(f"Saque: R$ {valor:.2f}")
        atualizar_saldo()
    else:
        messagebox.showerror("Erro", "O valor informado é inválido.")

def mostrar_extrato():
    if extrato:
        messagebox.showinfo("Extrato", extrato)
    else:
        messagebox.showinfo("Extrato", "Não foram realizadas movimentações.")

def atualizar_extrato(movimentacao):
    global extrato
    extrato += movimentacao + "\n"

def atualizar_saldo():
    label_saldo.config(text=f"Saldo: R$ {saldo:.2f}")

# Configurações iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Interface Gráfica
root = tk.Tk()
root.title("Sistema Bancário")

# Layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10, fill='both', expand=True)

label_saldo = tk.Label(frame, text=f"Saldo: R$ {saldo:.2f}", font=('Arial', 14))
label_saldo.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

label_valor = tk.Label(frame, text="Valor:")
label_valor.grid(row=1, column=0, sticky='e')

entry_valor = tk.Entry(frame)
entry_valor.grid(row=1, column=1, padx=5)

button_depositar = tk.Button(frame, text="Depositar", command=depositar)
button_depositar.grid(row=2, column=0, pady=5, padx=5, sticky='ew')

button_sacar = tk.Button(frame, text="Sacar", command=sacar)
button_sacar.grid(row=2, column=1, pady=5, padx=5, sticky='ew')

button_extrato = tk.Button(frame, text="Extrato", command=mostrar_extrato)
button_extrato.grid(row=3, column=0, columnspan=2, pady=5, padx=5, sticky='ew')

button_sair = tk.Button(frame, text="Sair", command=root.quit)
button_sair.grid(row=4, column=0, columnspan=2, pady=5, padx=5, sticky='ew')

# Ajusta o peso das colunas para expansão
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()