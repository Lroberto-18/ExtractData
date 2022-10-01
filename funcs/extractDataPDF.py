# Falta testar algumas funções
from funcs.imports import *

def main_menu():
    #windows: os.system("cls")
    #os.system("clear")
    print("1 - Extrair Imagens")
    print("2 - Extrair Textos paginas separdas")
    print("3 - Extrair Textos paginas em um arquivo txt")
    print("4 - Extrair Tabelas")
    print("5 - Sair")
    
def carregar_pdf(nome_pdf):
    Pdf = PdfReader(nome_pdf)
    return Pdf

def numero_paginas(pdf):
    numPag = len(pdf.pages)
    return numPag

def busca_por_pagina(numero_pagina, pdf):
    pagina_especifica = pdf.getPage(numero_pagina)
    return pagina_especifica

def mesclar_pdf(lista_pdf):
    mesclarPdf = PdfMerger()
    for pdf in lista_pdf:
        mesclarPdf.append(pdf)
    mesclarPdf.write("merged.pdf")
    mesclarPdf.close()

def pdf_em_txt(pdf):
    #salvar cada página em um arquivo TXT
    np = numero_paginas(pdf)
    for page in range(np):
        nome = str(page)
        arquivo = '.txt'
        paginaEspecifica = busca_por_pagina(page,pdf)
        conteudo = paginaEspecifica.extract_text()
        #salvar conteúdo em um TXT diferente
        with open(nome+arquivo, 'w') as arquivo:
            arquivo.write(str(conteudo))

def pdf_em_vetor(pdf):
    #array com o conteúdo de todas as páginas
    lista = []
    np = numero_paginas(pdf)
    page = 0
    for page in range(np):
        paginaEspecifica = busca_por_pagina(page,pdf)
        conteudo = paginaEspecifica.extract_text()
        lista.append(conteudo)
    #salvar todo conteúdo em um só arquivo TXT
    with open('final.txt', 'w') as arquivo:
        arquivo.write(str(lista))
    return lista

def pdf_em_vetor2(caminho):
    textos=[]
    #varios PDFs em um vetor
    arquivos = listdir(caminho)
    for i in range(len(arquivos)):
        aux = open(caminho + arquivos[i], 'rb')
        aux = PyPDF2.PdfFileReader(aux)
        for j in range(len(aux.pages)):
            textos[i] = textos[i] + aux.pages[j].extract_text()
    return textos

def pdf_imagens(caminho):
    imagem = [] #vetor com todas as imagens em forma de matriz
    arquivos = listdir(caminho)
    #Extrair imagens de varios pdf em uma pasta
    for i in range(len(arquivos)):
        file = caminho+'/'+arquivos[i]
        dir_img = str(arquivos[i].strip('.pdf'))
        os.mkdir(dir_img)
        pdf_file = fitz.open(file)
        print(f"Analisando o arquivo: {arquivos[i]}")
    
        for page_index in range(len(pdf_file)):
            page = pdf_file[page_index]
            image_list = page.getImageList()
            
            if image_list:
                print(f"{len(image_list)} imagens encontradas na página {page_index+1}")
            else:
                print("Nenhuma imagem encontrada na página", page_index+1)
                
            for image_index, img in enumerate(page.getImageList(), start=1):
                # 
                xref = img[0]
                # 
                base_image = pdf_file.extractImage(xref)
                image_bytes = base_image["image"]
                # 
                image_ext = base_image["ext"]
                #
                image = Image.open(io.BytesIO(image_bytes))
                #
                image.save(open(f"imagem{page_index+1}_{image_index}.{image_ext}", "wb"))
                img_name = 'imagem' + str(page_index+1) + '_' + str(image_index) + '.' + str(image_ext)
                imagem.append(imageio.imread(img_name))
                shutil.move(img_name,dir_img)
                print(f"Extraindo -> {dir_img}/{img_name}")
    return imagem
def pdf_tabelas(caminho):
    lista = []
    lista_tabelas = []
    arquivos = listdir(caminho)
    for i in range(len(arquivos)):
        file = caminho+'/'+arquivos[i]
        print(f"Analisando o arquivo: {arquivos[i]}")
                 
        lista_tabelas = tb.read_pdf(file, pages = "all")
        lista.append(lista_tabelas)
        j = 0
        for lista in lista_tabelas:
            nome = "p" + str(j) 
            f = ".xlsx"
            nome = nome + f 
            dados = pd.DataFrame(data= lista)
            dados.to_excel(nome, index = False)
            j+=1