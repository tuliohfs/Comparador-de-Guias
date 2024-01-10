import tkinter as tk
from tkinter import filedialog
import camelot
import tabula
import re

# Pilhas globais para armazenar os valores da mercon
pilha_lote_mercon = []
pilha_sacas_mercon = []
pilha_peso_mercon = []

# Pilhas globais para armazenar os valores do procafe
pilha_lote_procafe = []
pilha_sacas_procafe = []
pilha_peso_procafe = []

def extrair_dados_mercon():
    global pilha_lote_mercon, pilha_sacas_mercon, pilha_peso_mercon

    # Limpar o texto na área de texto
    text_label.delete(1.0, tk.END)

    # Obter o caminho do arquivo PDF
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if file_path:
        # Extrair tabelas do arquivo PDF usando Camelot
        tables = camelot.read_pdf(file_path, flavor='stream', pages='all')

        # Limpar as pilhas antes de uma nova extração
        pilha_lote_mercon = []
        pilha_sacas_mercon = []
        pilha_peso_mercon = []

        # Exibir tabelas na área de texto
        for table in tables:
            # Filtrar linhas usando a expressão regular
            filtered_rows = table.df[table.df[0].str.match(r'[A-Za-z]\d{5}-?\d{2}', na=False)]

            # Exibir apenas as colunas desejadas (Lotes, SACAS, PESO)
            filtered_rows = filtered_rows[[0, 3, 4]]

            # Armazenar valores nas pilhas globais
            pilha_lote_mercon.extend(filtered_rows.iloc[:, 0])
            pilha_sacas_mercon.extend(filtered_rows.iloc[:, 1])
            pilha_peso_mercon.extend(filtered_rows.iloc[:, 2])

        # Chamar a outra função para processar os dados (por exemplo, exibir em outra janela)
        processar_dados()

def extrair_dados_procafe():
    global pilha_lote_procafe, pilha_sacas_procafe, pilha_peso_procafe

    # Limpar o texto na área de texto
    text_label.delete(1.0, tk.END)

    # Obter o caminho do arquivo PDF
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    if file_path:
        # Extrair tabelas do arquivo PDF
        tables = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

        # Limpar as pilhas antes de uma nova extração
        pilha_lote_procafe = []
        pilha_sacas_procafe = []
        pilha_peso_procafe = []

        # Exibir apenas as linhas desejadas da Tabela 2
        for i, table in enumerate(tables, 1):
            if i == 2:  # Se for a Tabela 2
                # Filtrar linhas que correspondem ao padrão desejado na coluna 1
                filtered_rows = table[table.iloc[:, 0].astype(str).str.contains(r'[A-Za-z]\d{5}-?\d{2}', na=False)]



                # Armazenar dados nas pilhas globais
                pilha_lote_procafe.extend(filtered_rows.iloc[:, 0])
                pilha_sacas_procafe.extend(filtered_rows.iloc[:, 6])
                pilha_peso_procafe.extend(filtered_rows.iloc[:, 7])

        # Chamar a outra função para processar os dados (por exemplo, exibir em outra janela)
        processar_dados()

def processar_dados():
    # Função para processar os dados armazenados nas pilhas globais
    global pilha_lote_mercon, pilha_sacas_mercon, pilha_peso_mercon
    global pilha_lote_procafe, pilha_sacas_procafe, pilha_peso_procafe

    # Comparar os lotes e sacas dos dois conjuntos de dados
    for guia, saca_mercon, peso_mercon in zip(pilha_lote_mercon, pilha_sacas_mercon, pilha_peso_mercon):
        if guia in pilha_lote_procafe:
            index = pilha_lote_procafe.index(guia)
            saca_procafe = pilha_sacas_procafe[index]
            peso_procafe = pilha_peso_procafe[index]

            if saca_mercon == saca_procafe:
                text_label.insert(tk.END, f"Guia {guia} corresponde e tem o mesmo número de sacas {saca_mercon} e peso {peso_mercon} em ambos os conjuntos de dados.\n", "correspondente")
            else:
                text_label.insert(tk.END, f"Guia {guia} corresponde, mas tem números diferentes de sacas {saca_mercon} e {saca_procafe} e pesos {peso_mercon} e {peso_procafe} em ambos os conjuntos de dados.\n", "diferente")
        else:
            text_label.insert(tk.END, f"Guia {guia} não foi encontrado no segundo conjunto de dados.\n", "nao_encontrado")

    # Verificar se há guias no segundo conjunto de dados que não estão no primeiro conjunto de dados
    for guia in pilha_lote_procafe:
        if guia not in pilha_lote_mercon:
            text_label.insert(tk.END, f"Guia {guia} foi encontrado apenas no segundo conjunto de dados.\n", "apenas_no_segundo")


# Exemplo de uso
root = tk.Tk()
text_label = tk.Text(root)
text_label.pack()

button_mercon = tk.Button(root, text="Escolher Arquivo Mercon", command=extrair_dados_mercon)
button_mercon.pack()

button_procafe = tk.Button(root, text="Escolher Arquivo Procafe", command=extrair_dados_procafe)
button_procafe.pack()

root.mainloop()
