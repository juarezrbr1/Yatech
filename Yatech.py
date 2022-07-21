import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import os
import pandas as pd

pasta = r'C:\Python Scripts\banco_de_imagens'

# Cria lista de imagens e questões em texto
banco_imagens = []
questoes_str = []


def listar_imagens():
    # Lista as imagens
    for nome in os.listdir(pasta):
        nome_ = "\\" + nome
        arquivo = pasta + nome_
        arquivo.replace(' ', '')
        banco_imagens.append(arquivo)


def extrair_texto_lista():
    # Extrai texto das imagens listadas
    for imagens in banco_imagens:
        imag = Image.open(imagens)
        texto = tess.image_to_string(imag, lang="por")
        questoes_str.append(texto)


listar_imagens()
extrair_texto_lista()

df = pd.DataFrame(questoes_str)
df.to_excel(r'C:\Python Scripts\venv\teste.xlsx')