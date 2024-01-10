import tkinter as tk
from tkinter import *
from tkinter import filedialog
import customtkinter

def comparar_dado_mercon():

def comparar_dado_sucafina():
    # Criar uma janela para o PDF SUCAFINA
    janela_sucafina = customtkinter.CTk()
    janela_sucafina.title("Comparação de Lotes e Sacas")
    janela_sucafina.geometry("850x550")
    janela_sucafina._set_appearance_mode("dark")
    janela_sucafina.resizable(False, False)
    janela_sucafina.iconbitmap("C:/Program Files/pdf-liv/IMG/icon.ico")  # Importando logo da Empresa

    # Criar campos de entrada de texto para os nomes dos arquivos PDF
    quadro1 = customtkinter.CTkFrame(janela_sucafina, fg_color="#242424")
    quadro1.pack(pady=10)

    rotulo_pdf1 = customtkinter.CTkLabel(quadro1, text="PDF PROCAFE:", text_color="white")
    rotulo_pdf1.pack(side=tk.LEFT)

    entrada_pdf1 = customtkinter.CTkEntry(quadro1)
    entrada_pdf1.pack(side=tk.LEFT, padx=10)

    quadro2 = customtkinter.CTkFrame(janela_sucafina, fg_color="#242424")
    quadro2.pack(pady=10)

    rotulo_pdf2 = customtkinter.CTkLabel(quadro2, text="PDF SUCAFINA:", text_color="white")
    rotulo_pdf2.pack(side=tk.LEFT)

    entrada_pdf2 = customtkinter.CTkEntry(quadro2)
    entrada_pdf2.pack(side=tk.LEFT, padx=10)

    # Botão para selecionar os arquivos PDF
    def selecionar_arquivo1():
        arquivo1 = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        entrada_pdf1.delete(0, tk.END)
        entrada_pdf1.insert(0, arquivo1)

    def selecionar_arquivo2():
        arquivo2 = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        entrada_pdf2.delete(0, tk.END)
        entrada_pdf2.insert(0, arquivo2)

    botao_selecionar1 = customtkinter.CTkButton(quadro1, text="Selecionar", command=selecionar_arquivo1, fg_color="#263d76")
    botao_selecionar1.pack(side=tk.RIGHT)

    botao_selecionar2 = customtkinter.CTkButton(quadro2, text="Selecionar", command=selecionar_arquivo2, fg_color="#263d76")
    botao_selecionar2.pack(side=tk.RIGHT)

    # Botão para processar os arquivos PDF e comparar os lotes e sacas
    botao_processar = customtkinter.CTkButton(janela_sucafina, text="Processar", command="", bg_color="#242424", fg_color="#263d76")
    botao_processar.pack(pady=10)

    # Widget de resultado com barra de rolagem
    quadro_resultado = customtkinter.CTkFrame(janela_sucafina)
    quadro_resultado.pack(fill=tk.BOTH, expand=True)

    barra_rolagem_resultado = customtkinter.CTkScrollbar(quadro_resultado, bg_color="#242424")
    barra_rolagem_resultado.pack(side=tk.RIGHT, fill=tk.Y)

    resultado = tk.Text(quadro_resultado, wrap=tk.WORD, yscrollcommand=barra_rolagem_resultado.set)
    resultado.pack(fill=tk.BOTH, expand=True)

    barra_rolagem_resultado.configure(command=resultado.yview)

    # Definir estilos de texto
    resultado.tag_configure("correspondente", foreground="black")
    resultado.tag_configure("diferente", foreground="#61081b")
    resultado.tag_configure("nao_encontrado", foreground="#073abc")
    resultado.tag_configure("apenas_no_segundo", foreground="#671479")

    # Iniciar o loop principal da interface gráfica
    janela_sucafina.mainloop()
    
def comparar_dado_white():
    # Criar uma janela para o PDF WHITE
    janela_white = customtkinter.CTk()
    janela_white.title("Comparação de Lotes e Sacas")
    janela_white.geometry("850x550")
    janela_white._set_appearance_mode("dark")
    janela_white.resizable(False, False)
    janela_white.iconbitmap("C:/Program Files/pdf-liv/IMG/icon.ico")  # Importando logo da Empresa

    # Criar campos de entrada de texto para os nomes dos arquivos PDF
    quadro1 = customtkinter.CTkFrame(janela_white, fg_color="#242424")
    quadro1.pack(pady=10)

    rotulo_pdf1 = customtkinter.CTkLabel(quadro1, text="PDF PROCAFE:", text_color="white")
    rotulo_pdf1.pack(side=tk.LEFT)

    entrada_pdf1 = customtkinter.CTkEntry(quadro1)
    entrada_pdf1.pack(side=tk.LEFT, padx=10)

    quadro2 = customtkinter.CTkFrame(janela_white, fg_color="#242424")
    quadro2.pack(pady=10)

    rotulo_pdf2 = customtkinter.CTkLabel(quadro2, text="PDF WHITE:", text_color="white")
    rotulo_pdf2.pack(side=tk.LEFT)

    entrada_pdf2 = customtkinter.CTkEntry(quadro2)
    entrada_pdf2.pack(side=tk.LEFT, padx=10)

    # Botão para selecionar os arquivos PDF
    def selecionar_arquivo1():
        arquivo1 = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        entrada_pdf1.delete(0, tk.END)
        entrada_pdf1.insert(0, arquivo1)

    def selecionar_arquivo2():
        arquivo2 = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
        entrada_pdf2.delete(0, tk.END)
        entrada_pdf2.insert(0, arquivo2)

    botao_selecionar1 = customtkinter.CTkButton(quadro1, text="Selecionar", command=selecionar_arquivo1, fg_color="#263d76")
    botao_selecionar1.pack(side=tk.RIGHT)

    botao_selecionar2 = customtkinter.CTkButton(quadro2, text="Selecionar", command=selecionar_arquivo2, fg_color="#263d76")
    botao_selecionar2.pack(side=tk.RIGHT)

    # Botão para processar os arquivos PDF e comparar os lotes e sacas
    botao_processar = customtkinter.CTkButton(janela_white, text="Processar", command="", bg_color="#242424", fg_color="#263d76")
    botao_processar.pack(pady=10)

    # Widget de resultado com barra de rolagem
    quadro_resultado = customtkinter.CTkFrame(janela_white)
    quadro_resultado.pack(fill=tk.BOTH, expand=True)

    barra_rolagem_resultado = customtkinter.CTkScrollbar(quadro_resultado, bg_color="#242424")
    barra_rolagem_resultado.pack(side=tk.RIGHT, fill=tk.Y)

    resultado = tk.Text(quadro_resultado, wrap=tk.WORD, yscrollcommand=barra_rolagem_resultado.set)
    resultado.pack(fill=tk.BOTH, expand=True)

    barra_rolagem_resultado.configure(command=resultado.yview)

    # Definir estilos de texto
    resultado.tag_configure("correspondente", foreground="black")
    resultado.tag_configure("diferente", foreground="#61081b")
    resultado.tag_configure("nao_encontrado", foreground="#073abc")
    resultado.tag_configure("apenas_no_segundo", foreground="#671479")

    # Iniciar o loop principal da interface gráfica
    janela_white.mainloop()
    
def janela_principal():
    # Configurando a janela principal
    main = customtkinter.CTk()  # Criar janela
    main.title("Comparação de Lotes e Sacas")  # Definir titulo da janela
    main.geometry("850x550")  # Definindo tamanho da janela
    main._set_appearance_mode("dark")  # Definindo Tema da Janela
    main.resizable(False, False)  # Definindo padrão para não possibilitar o redimensionamento da janela
    main.iconbitmap("C:/Program Files/pdf-liv/IMG/icon.ico")  # Importando logo da Empresa

    # Carregar imagem Logo
    imagem_original = PhotoImage(file="C:/Program Files/pdf-liv/IMG/logo-livlogistica.png")
    imagem_label = tk.Label(main, image=imagem_original, bg="#242424")
    imagem_label.pack(pady=10)

    # Criando e posicionando botões na janela principal
    # Botão para abrir janela Mercon
    botao_mercon = customtkinter.CTkButton(main, text="Mercon", command=comparar_dado_mercon , bg_color="#242424", fg_color="#263d76")
    botao_mercon.pack(pady=10)

    # Botão para abrir janela Sucafina
    botao_sucafina = customtkinter.CTkButton(main, text="Sucafina", command=comparar_dado_sucafina , bg_color="#242424", fg_color="#263d76")
    botao_sucafina.pack(pady=10)

    # Botão para abrir janela White
    botao_white = customtkinter.CTkButton(main, text="White", command=comparar_dado_white , bg_color="#242424", fg_color="#263d76")
    botao_white.pack(pady=10)

    # Iniciando o loop principal
    main.mainloop()

# Chamar a função para configurar e exibir a janela principal
janela_principal()
