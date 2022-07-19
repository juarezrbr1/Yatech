import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

imagem_teste = Image.open('pag2.PNG')


def tratamento_imagem():
    # tipando a leitura para os canais de ordem RGB
    imagem = Image.open('pag2.PNG').convert('RGB')

    # convertendo em um array editável de numpy[x, y, CANALS]
    npimagem = np.asarray(imagem).astype(np.uint8)

    # diminuição dos ruidos antes da binarização
    npimagem[:, :, 0] = 0  # zerando o canal R (RED)
    npimagem[:, :, 1] = 0  # zerando o canal B (BLUE)

    # atribuição em escala de cinza
    im = cv.cvtColor(npimagem, cv.COLOR_RGB2GRAY)

    # aplicação da truncagem binária para a intensidade
    # pixels de intensidade de cor abaixo de 127 serão convertidos para 0 (PRETO)
    # pixels de intensidade de cor acima de 127 serão convertidos para 255 (BRANCO)
    # A atrubição do THRESH_OTSU incrementa uma análise inteligente dos nivels de truncagem
    ret, thresh = cv.threshold(im, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    # reconvertendo o retorno do threshold em um objeto do tipo PIL.Image
    binimagem = Image.fromarray(thresh)

    # chamada ao tesseract OCR por meio de seu wrapper
    phrase = tess.image_to_string(binimagem, lang='por')
    print(phrase)


tratamento_imagem()

print(20*'*-')

def extrair_texto():
    # Extrai texto da imagem
    texto = tess.image_to_string(imagem_teste, lang="por")
    print(texto)

# extrair_texto()