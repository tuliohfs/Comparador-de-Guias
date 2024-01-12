import tkinter as tk
from tkinter import ttk, filedialog
import tabula
import re

def extract_tables():
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
                # Filtrar linhas que correspondem ao padrão desejado na coluna 1
                filtered_rows = table[table.iloc[:, 0].str.contains(r'[A-Za-z]\d{5}-?\d{2}', na=False)]

                # Armazenar dados nas pilhas
                guias_stack.extend(filtered_rows.iloc[:, 0])
                sacas_stack.extend(filtered_rows.iloc[:, 6])
                peso_stack.extend(filtered_rows.iloc[:, 7])

        # Formatar e exibir os dados armazenados
        # Formatar e exibir os dados armazenados
        for guia, saca, peso in zip(guias_stack, sacas_stack, peso_stack):
            guia_match = re.search(r'[A-Za-z]\d{5}-?\d{2}', guia)
            guia_formatted = guia_match.group() if guia_match else "N/A"
            text.insert(tk.END, "Lote: {}, Sacas: {}, Peso: {}\n".format(guia_formatted, saca, peso))


# Criar a janela principal
root = tk.Tk()
root.title("Extrair Tabelas de PDF")

# Botão para selecionar arquivo PDF
browse_button = ttk.Button(root, text="Selecionar Arquivo PDF", command=extract_tables)
browse_button.pack(pady=10)

# Área de texto para exibir as tabelas
text = tk.Text(root, wrap="none", height=40, width=100)
text.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
