import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2 import PdfFileMerger
import sys
import tempfile
import shutil
import os
import ctypes

def msgbox(mensagem, icone, titulo):

    # // CRIA UMA MENSAGEM DE TEXTO PARA O USUARIO
    # // FUNCAO QUE CRIA UM MSGBOX
    '''
    P/ CRIAR LINHA - >  & vbCrLf & "
    0 = OK button only
    1 = OK and Cancel buttons
    2 = Abort, Retry, and Ignore buttons
    3 = Yes, No, and Cancel buttons
    4 = Yes and No buttons
    5 = Retry and Cancel buttons
    16 = Critical Message icon
    32 = Warning Query icon
    48 = Warning Message icon
    64 = Information Message icon
    0 = First button is default
    256 = Second button is default
    512 = Third button is default
    768 = Fourth button is default
    0 = Application modal
    4096 = System modal
    '''
    MessageBox = ctypes.windll.user32.MessageBoxW
    return MessageBox(None, mensagem, titulo, int(icone) | 4096)

argumentos = sys.argv
dir_pdf = False
arquivos_pdf = []
number_of_pages = 0

for i in argumentos:
    if os.path.isfile(i) and i.upper().endswith('.PDF'):
        dir_pdf = os.path.dirname(i)
        break

if not dir_pdf:
    msgbox("O Arquivo selecionado não é PDF", 48, "Erro")
    sys.exit(0)


for i in os.listdir(dir_pdf):
    if str(i).upper().endswith('.PDF'):
        arquivos_pdf.append(i)

paginas = 0

for i in arquivos_pdf:
    path = os.path.join(dir_pdf, i)
    with open(path, 'rb') as pdf_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()        
        paginas += number_of_pages

msgbox('O diretorio do arquivo selecionado tem {0} paginas PDF.'.format(paginas), 48, 'Sucesso')
sys.exit(0)
