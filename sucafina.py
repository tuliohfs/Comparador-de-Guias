import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pdfplumber
import re

def extract_tables():
    arquivo_cliente = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    lotes_cliente = []
    sacas_cliente = []
    pesos_cliente = []

    with pdfplumber.open(arquivo_cliente) as pdf1:
        for page in pdf1.pages:
            text = page.extract_text()

            for line in text.split('\n'):
                parts = line.strip().split()
                if len(parts) >= 7:
                    lote_match = re.search(r'[A-Za-z]\d{5}-?\d{2}', line.strip())
                    sacas_match = re.findall(r'\b\d{3}\b', parts[2])
                    peso_match = re.findall(r'\d{2}[.,]\d{3}', parts[6])

                    if lote_match and sacas_match and peso_match:
                        lotes_cliente.append(lote_match.group(0))
                        sacas_cliente.append(sacas_match[0])
                        pesos_cliente.append(peso_match[0])

    # Limpar a área de texto antes de exibir os resultados
    text_resultado.delete("1.0", tk.END)

    # Exibir os resultados na área de texto da interface gráfica
    for i in range(len(lotes_cliente)):
        text_resultado.insert(tk.END, f"Lote: {lotes_cliente[i]}, Sacas: {sacas_cliente[i]}, Peso: {pesos_cliente[i]}\n")

# Criar a janela principal
root = tk.Tk()
root.title("Extrair Tabelas de PDF")

# Botão para selecionar arquivo PDF
browse_button = ttk.Button(root, text="Selecionar Arquivo PDF", command=extract_tables)
browse_button.pack(pady=10)

# Área de texto para exibir as tabelas
text_resultado = tk.Text(root, wrap="none", height=40, width=100)
text_resultado.pack(padx=10, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
