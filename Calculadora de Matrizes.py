'''Caio Bastos RA:22402182
   Isaac Linhares RA:22407506
'''
from tkinter import *
from tkinter import messagebox

# Lista para armazenar widgets dinâmicos
widgets_extras = []
# Função para esconder todos os widgets extras
def esconder_widgets_extras():
    global widgets_extras
    for widget in widgets_extras:
        widget.grid_forget()
    widgets_extras.clear()
# Função para calcular operações com matrizes
def calcular_matriz(operacao):
    try:
        esconder_widgets_extras()
        matriz_a = [[int(entrada[i][j].get()) for j in range(2)] for i in range(2)]
        matriz_b = [[int(matriz2[i][j].get()) for j in range(2)] for i in range(2)]

        resultado_matriz = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                if operacao == "soma":
                    resultado_matriz[i][j] = matriz_a[i][j] + matriz_b[i][j]
                elif operacao == "sub":
                    resultado_matriz[i][j] = matriz_a[i][j] - matriz_b[i][j]
                elif operacao == "mult":
                    resultado_matriz[i][j] = sum(matriz_a[i][k] * matriz_b[k][j] for k in range(2))
                resultado[i][j].config(text=str(resultado_matriz[i][j]))
        mostrar_resultados()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números inteiros nas matrizes.")

# Função para calcular multiplicação escalar
def calcular_escalar():
    try:
        esconder_widgets_extras()
        escalar = int(escalar_var.get())
        for i in range(2):
            for j in range(2):
                valor = int(entrada[i][j].get()) * escalar
                resultado[i][j].config(text=str(valor))
        mostrar_resultados()
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido para o escalar.")

# Função para exibir campos da segunda matriz
def exibir_matriz2(operacao):
    esconder_widgets_extras()
    label_matriz2=Label(root, text="Insira a segunda matriz:")
    label_matriz2.grid(column=0, row=5, columnspan=4)
    widgets_extras.append(label_matriz2)
    for i in range(2):
        for j in range(2):
            matriz2[i][j] = Entry(root, width=7)
            matriz2[i][j].grid(column=j+1, row=i+6)
            widgets_extras.append(matriz2[i][j])
    botao_calcular = Button(root, text="Calcular", command=lambda: calcular_matriz(operacao))
    botao_calcular.grid(column=3, row=6, columnspan=4)
    widgets_extras.append(botao_calcular)


    botao_voltar=Button(root, text="Voltar", command=lambda:esconder_widgets_extras())
    botao_voltar.grid(column=3, row=7, columnspan=4)
    widgets_extras.append(botao_voltar)
# Função para exibir campo do escalar
def exibir_escalar_input():
    esconder_widgets_extras()
    label_escalar=Label(root, text="Insira o escalar:")
    label_escalar.grid(column=0, row=5, columnspan=2)
    widgets_extras.append(label_escalar)


    escalar_input.grid(column=2, row=5)
    widgets_extras.append(escalar_input)
    botao_calcular_escalar = Button(root, text="Calcular Escalar", command=calcular_escalar)
    botao_calcular_escalar.grid(column=4, row=5)


    botao_voltar=Button(root, text="Voltar", command=lambda: esconder_widgets_extras())
    widgets_extras.append(botao_calcular_escalar)
    botao_voltar.grid(column=3, row=7, columnspan=4)
    widgets_extras.append(botao_voltar)
def mostrar_resultados():
    for i in range(2):
        for j in range(2):
            resultado[i][j].grid(column=j+1, row=i+8)

# Configuração inicial da janela
root = Tk()
root.title("Calculadora de Matriz")
root.geometry('400x300')

# Variáveis
entrada = [[None for _ in range(2)] for _ in range(2)]
matriz2 = [[None for _ in range(2)] for _ in range(2)]
resultado = [[None for _ in range(2)] for _ in range(2)]
escalar_var = StringVar()

# Criar entradas para a matriz inicial
Label(root, text="Insira a matriz inicial:").grid(column=0, row=0, columnspan=4)
for i in range(2):
    for j in range(2):
        entrada[i][j] = Entry(root, width=7)
        entrada[i][j].grid(column=j+1, row=i+1)
        resultado[i][j] = Label(root, text="0", width=7)

# Botões para operações
Button(root, text="Soma de Matrizes", command=lambda: exibir_matriz2("soma")).grid(column=1, row=3)
Button(root, text="Subtração de Matrizes", command=lambda: exibir_matriz2("sub")).grid(column=2, row=3)
Button(root, text="Multiplicação Escalar", command=exibir_escalar_input).grid(column=1, row=4)
Button(root, text="Multiplicação de Matrizes", command=lambda: exibir_matriz2("mult")).grid(column=2, row=4)

# Campo do escalar
escalar_input = Entry(root, textvariable=escalar_var, width=7)

# Rodar a interface
root.mainloop()
