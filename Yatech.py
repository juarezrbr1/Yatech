import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

imagem_teste = Image.open('pag2.PNG')

def extrair_texto():
    # Extrai texto da imagem
    texto = tess.image_to_string(imagem_teste, lang="por")
    print(texto)


extrair_texto()
