import tkinter as tk
from tkinter import ttk, filedialog
import camelot
import re

def extrair_dados_mercon():
    # Limpar o texto na área de texto
    text_label.delete(1.0, tk.END)

    # Obter o caminho do arquivo PDF
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if file_path:
        # Extrair tabelas do arquivo PDF usando Camelot
        tables = camelot.read_pdf(file_path, flavor='stream', pages='all')

        # Pilhas para armazenar os valores de cada coluna
        guias_stack = []
        sacas_stack = []
        pesos_stack = []

        # Exibir tabelas na área de texto
        for i, table in enumerate(tables, 1):
            text_label.insert(tk.END, f"Tabela {i}:\n")
            
            # Filtrar linhas usando a expressão regular
            filtered_rows = table.df[table.df[0].str.match(r'[A-Za-z]\d{5}-?\d{2}', na=False)]

            # Exibir apenas as colunas desejadas (Lotes, SACAS, PESO)
            filtered_rows[[0, 3, 4]]

            # Armazenar valores em suas respectivas pilhas
            guias_stack.extend(filtered_rows.iloc[:, 0])
            sacas_stack.extend(filtered_rows.iloc[:, 3])
            pesos_stack.extend(filtered_rows.iloc[:, 4])

        for guia, saca, peso in zip(guias_stack, sacas_stack, pesos_stack):
            guia_match = re.search(r'[A-Za-z]\d{5}-?\d{2}', guia)
            guia_formatted = guia_match.group() if guia_match else "N/A"
            text_label.insert(tk.END, "Guia: {}, Sacas: {}, Peso: {}\n".format(guia_formatted, saca, peso))

# Criar a janela principal
janela_mercon = tk.Tk()
janela_mercon.title("Extrair Tabelas de PDF")

# Botão para selecionar arquivo PDF
extrair_button = ttk.Button(janela_mercon, text="Selecionar Arquivo PDF", command=extrair_dados_mercon)
extrair_button.pack(pady=10)

# Área de texto para exibir as tabelas
text_label = tk.Text(janela_mercon, wrap="none", height=20, width=80)
text_label.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
janela_mercon.mainloop()
