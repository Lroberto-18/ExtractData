# Manipulando PDF com python
# Mineração de Dados (Textos, Tabelas e Imagens)
# Linux mint 
# #pip install PyMuPDF==1.18.0

from funcs.extractDataPDF import *

#arquivo = carregar_pdf("pdf/RF01.pdf")

#teste função
#print("Número de páginas")
#print(numero_paginas(arquivo))
#a = pdf_imagens('./pdf')
#print(a[2])

#Menu de ações
var_control = 0
while var_control !=5:
	main_menu()
	var_control = int(input("Digite um numero "))
		
	if var_control == 1:
        #a = pdf_imagens('./pdf')
		print("OK")
	elif var_control == 2:
		print("OK")
	elif var_control == 3:
		print("OK")
	elif var_control == 4:
		print("OK")
	elif var_control == 5:
		os.system("clear")
		print("finalizado ")
	else:
		os.system("clear")
		print("Opção inválida ")