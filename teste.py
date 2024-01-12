import tkinter as tk
from tkinter import ttk, filedialog
import tabula
import re
import sqlite3

def create_table_if_not_exists():
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect("dados_extracao.db")
    cursor = conn.cursor()

    # Criar tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS extracoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            identificador TEXT,
            guia TEXT,
            saca INTEGER,
            peso INTEGER
        )
    ''')

    # Commit e fechar a conexão
    conn.commit()
    conn.close()

def extract_tables(identificador):
    # Limpar o texto na área de texto
    text.delete(1.0, tk.END)

    # Obter o caminho do arquivo PDF
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if file_path:
        # Extrair tabelas do arquivo PDF
        tables = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

        # Inicializar pilhas para armazenar dados
        guias_stack = []
        sacas_stack = []
        peso_stack = []

        # Exibir apenas as linhas desejadas da Tabela 2
    for i, table in enumerate(tables, 1):
        if i == 2:  # Se for a Tabela 2
            # Converter a coluna para o tipo de dados string antes de aplicar contains
            table.iloc[:, 0] = table.iloc[:, 0].astype(str)

            # Filtrar linhas que correspondem ao padrão desejado na coluna 1
            filtered_rows = table[table.iloc[:, 0].str.contains(r'[A-Za-z]\d{5}-?\d{2}', na=False)]

            # Restaurar o tipo de dados original da coluna
            table.iloc[:, 0] = table.iloc[:, 0].astype(object)

            # Armazenar dados nas pilhas
            guias_stack.extend(filtered_rows.iloc[:, 0])
            sacas_stack.extend(filtered_rows.iloc[:, 6])
            peso_stack.extend(filtered_rows.iloc[:, 7])


        # Conectar ao banco de dados SQLite
        conn = sqlite3.connect("dados_extracao.db")
        cursor = conn.cursor()

        # Inserir dados na tabela
        for guia, saca, peso in zip(guias_stack, sacas_stack, peso_stack):
            guia_match = re.search(r'[A-Za-z]\d{5}-?\d{2}', guia)
            guia_formatted = guia_match.group() if guia_match else "N/A"

            # Inserir dados na tabela
            cursor.execute("INSERT INTO extracoes (identificador, guia, saca, peso) VALUES (?, ?, ?, ?)",
                           (identificador, guia_formatted, saca, peso))

            # Exibir na área de texto
            text.insert(tk.END, "Lote: {}, Sacas: {}, Peso: {}\n".format(guia_formatted, saca, peso))

        # Commit e fechar a conexão
        conn.commit()
        conn.close()

def on_identificador_entry_change(*args):
    global identificador_entry_text
    identificador_entry_text = identificador_entry_var.get()

# Criar a janela principal
root = tk.Tk()
root.title("Extrair Tabelas de PDF")

# Criar tabela se não existir
create_table_if_not_exists()

# Campo de entrada para identificador
identificador_label = ttk.Label(root, text="Identificador:")
identificador_label.pack(pady=5)

identificador_entry_var = tk.StringVar()
identificador_entry = ttk.Entry(root, textvariable=identificador_entry_var)
identificador_entry.pack(pady=5)
identificador_entry_var.trace_add("write", on_identificador_entry_change)

# Botão para selecionar arquivo PDF
browse_button = ttk.Button(root, text="Selecionar Arquivo PDF", command=lambda: extract_tables(identificador_entry_var.get()))
browse_button.pack(pady=10)

# Área de texto para exibir as tabelas
text = tk.Text(root, wrap="none", height=40, width=100)
text.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
