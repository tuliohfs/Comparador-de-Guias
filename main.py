import tkinter as tk
from tkinter import ttk, filedialog
import tabula
import re

def janela_mercon():
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
            for guia, saca, peso in zip(guias_stack, sacas_stack, peso_stack):
                guia_match = re.search(r'[A-Za-z]\d{5}-?\d{2}', guia)
                guia_formatted = guia_match.group() if guia_match else "N/A"
                text.insert(tk.END, "Guia: {}, Sacas: {}, Peso: {}\n".format(guia_formatted, saca, peso))

    # Criar a janela principal
    root = tk.Tk()
    root.title("Janela Mercon")

    # Botão para selecionar arquivo PDF
    browse_button = ttk.Button(root, text="Selecionar Arquivo PDF", command=extract_tables)
    browse_button.pack(pady=10)

    # Área de texto para exibir as tabelas
    text = tk.Text(root, wrap="none", height=40, width=100)
    text.pack(padx=10, pady=10)

    # Iniciar o loop principal da interface gráfica
    root.mainloop()


def abrir_janela(titulo):
    nova_janela = tk.Toplevel(root)
    nova_janela.title(titulo)
    # Adicione widgets e lógica para a nova janela aqui

# Configurando a janela principal
root = tk.Tk()
root.title("Menu Principal")

# Criando e posicionando botões na janela principal
botao_janela1 = tk.Button(root, text="Abrir Janela 1", command=janela_mercon)
botao_janela1.pack(pady=10)

botao_janela2 = tk.Button(root, text="Abrir Janela 2", command=lambda: abrir_janela("Janela 2"))
botao_janela2.pack(pady=10)

botao_janela3 = tk.Button(root, text="Abrir Janela 3", command=lambda: abrir_janela("Janela 3"))
botao_janela3.pack(pady=10)

# Iniciando o loop principal
root.mainloop()
