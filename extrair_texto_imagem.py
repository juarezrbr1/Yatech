import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image, ImageEnhance
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

pasta = r'C:\Users\juare\Documents\Python Scripts\banco_de_imagens'

imagem_teste = Image.open(r'C:\Users\juare\Documents\Python Scripts\banco_de_imagens\pag2.png')
# imag = cv2.imread('imagem_nova.jpg')
# imag.show()

def duno_filtro():
    sharpness = ImageEnhance.Sharpness(imag)
    sharpnessed = sharpness.enhance(1)
    saturacao = ImageEnhance.Color(sharpnessed)
    saturadada = saturacao.enhance(1)
    brilho = ImageEnhance.Brightness(saturadada)
    brilhante = brilho.enhance(1.2)
    contraste = ImageEnhance.Contrast(brilhante)
    contrastada = contraste.enhance(1.5)
    contrastada.save(r'C:\Users\juare\Documents\Python Scripts\banco_de_imagens\pag2_nova.png')
    texto = tess.image_to_string(contrastada, lang="por")
    print(texto)


def clarear_imagem():
    filtro_1 = np.ones(imagem_teste.shape, dtype=np.uint8) * 110
    somada = cv2.cv2.add(imagem_teste, filtro_1)
    cv2.imshow('somada',somada)
    cv2.cv2.waitKey(0)
    cv2.cv2.destroyWindow()


clarear_imagem()


def escurecer_imagem():
    filtro_2 = np.ones(imagem_teste.shape, dtype=np.uint8) * 110
    subtraida = cv2.cv2.subtract(imagem_teste, filtro_2)
    cv2.imshow('subtraida', subtraida)
    cv2.cv2.waitKey(0)
    cv2.cv2.destroyWindow()



def sharpening():
    kernel_sharpening_1 = np.array([[-1, -1, -1],
                                    [-1, 9, -1],
                                    [-1, -1, -1]])
    sharpened = cv2.cv2.filter2D(imagem_teste, -1, kernel_sharpening_1)
    cv2.imshow('sharpened', sharpened)
    cv2.cv2.waitKey(0)
    cv2.cv2.destroyWindow()


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

def limpaimg(img1, novaimg):
    # Limpa a imagem
    img = Image.open(img1)
    img = img.point(lambda x: 0 if x < 100 else 255)
    img.save(novaimg)
    return img


# limpaimg(r'C:\Users\juare\Documents\Python Scripts\banco_de_imagens\pag2.png', r'C:\Users\juare\Documents\Python Scripts\banco_de_imagens\pag2_nova.png')

def extrair_texto_lista():
    # Extrai texto das imagens listadas
    for imagens in banco_imagens:
        imag = Image.open(imagens)
        # imag = cv2.imread('imagem_nova.jpg')
        texto = tess.image_to_string(imag, lang="por")
        questoes_str.append(texto)

# df = pd.DataFrame(questoes_str)
# df.to_excel('teste.xlsx')


imagem_curso = cv.imread(r'C:\Users\juare\OneDrive\Documentos\Visao computacional em Python\Códigos Udemy para alunos'
                         r'\Códigos Udemy para alunos_\3 - Pre-Processamento\Imagens\Cinza.jpg')

