import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import openpyxl
import xlrd
import re

def extract_data(file_path):
    # Função para extrair dados específicos do arquivo Excel
    # Adicione aqui a lógica para extrair lotes, volume e peso
    try:
        wb = openpyxl.load_workbook(file_path)
    except openpyxl.utils.exceptions.InvalidFileException:
        # Se falhar, tenta usar xlrd para abrir o arquivo .xls
        wb = xlrd.open_workbook(file_path)

    sheet = wb.active if isinstance(wb, openpyxl.workbook.workbook.Workbook) else wb.sheet_by_index(0)
    data = []

    for row_index in range(sheet.nrows):
        for col_index in range(sheet.ncols):
            cell_value = sheet.cell_value(row_index, col_index)
            # Procurar por lotes usando expressão regular
            match = re.search(r'[A-Za-z]\d{5}-?\d{2}', str(cell_value))
            if match:
                lote = match.group()
                # Verificar se há células suficientes para obter volume e peso
                if col_index + 2 < sheet.ncols:
                    volume = sheet.cell_value(row_index, col_index + 1)
                    peso = sheet.cell_value(row_index, col_index + 3)
                    data.append((lote, volume, peso))
                break

    return data

def select_file():
    # Função para selecionar o arquivo Excel
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    if file_path:
        data = extract_data(file_path)
        display_data(data)

def display_data(data):
    # Função para exibir dados na área de texto
    text.delete(1.0, tk.END)  # Limpa o conteúdo atual da área de texto
    for item in data:
        text.insert(tk.END, f"Lote: {item[0]}, Sacas: {item[1]}, Peso: {item[2]}\n")

# Criar a janela principal
root = tk.Tk()
root.title("Extrair Dados Específicos de Excel")

# Botão para selecionar arquivo Excel
browse_button = ttk.Button(root, text="Selecionar Arquivo Excel", command=select_file)
browse_button.pack(pady=10)

# Área de texto para exibir as tabelas
text = tk.Text(root, wrap="none", height=40, width=100)
text.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
