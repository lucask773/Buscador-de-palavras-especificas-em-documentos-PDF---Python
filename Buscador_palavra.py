import PyPDF2
import re
import os

def encontrar_palavras_especificas(pdf_file, palavras):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_paginas = len(reader.pages)

        for palavra in palavras:
            total_ocorrencias = 0

            for pagina_num in range(num_paginas):
                pagina = reader.pages[pagina_num]
                texto = pagina.extract_text()
                
                ocorrencias = re.findall(palavra, texto, re.IGNORECASE)
                total_ocorrencias += len(ocorrencias)
                print(f"Palavra '{palavra}': {len(ocorrencias)} ocorrências na página {pagina_num + 1}")

            print(f"A palavra '{palavra}' foi encontrada {total_ocorrencias} vezes.")

# Arquivo PDF e palavras específicas a serem encontradas
diretorio_atual = os.getcwd()
pdf_file = os.path.join(diretorio_atual, r'COLOCAR DESTINO DO PDF SELECIONADO')
palavras = ['COLOCAR PALAVRA QUE DESEJA BUSCAR']

# Chamada da função para encontrar as palavras específicas
encontrar_palavras_especificas(pdf_file, palavras)

