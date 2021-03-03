import os
from time import sleep

def clear():
	return os.system('clear') or None

def linha():
	print('—' *40)

def cor(msg):
	verde = '\033[32m'
	vermelho = '\033[31m'
	branco = '\033[m'
	if msg == 'VERDE':
		return verde
	elif msg == 'VERMELHO':
		return vermelho
	elif msg == 'BRANCO':
		return branco
	
def salvar(var, str, str2, str3):
	var.append(str)
	var.append(str2)
	var.append(str3)
	
def style_txt(txt):
	if txt == 'Sistema de cadastros':
		tamanho = len(txt) + 12
		print('-' *tamanho)
		print(f'      {txt}')
		print('-' *tamanho)
	else:
		tamanho = len(txt) + 12
		print('-' *tamanho)
		print(f'      {txt}')
		print('-' *tamanho)
	
def save_txt(param):
	with open('Cadastros.txt', 'a') as arquivo:
		for p in param:
			arquivo.writelines(f'Nome: {p[0]}\nIdade: {p[1]}\nSexo: {p[2]}\n=======\n')
			print('Salvando...')
			sleep(2)
			clear()

def masculino(v):
	for pessoa in v:
		if pessoa[2] == 'M':
			print(pessoa[0:2])
				
def menu():
	while True:
		style_txt('Sistema de cadastros')	
		print('[ 1 ] Cadastrar uma nova pessoa\n[ 2 ] Ver cadastrados\n[ 3 ] Ver mulheres cadastradas\n[ 4 ] Ver homens cadastrados\n[ 5 ] Salvar em um arquivo txt\n[ 6 ] Sair do programa')
		info_menu = int(input('Sua opção: '))
		if info_menu == 1:
			informacoes = pede_info()
		elif info_menu == 5:
			save_txt(informacoes)
			continue
		elif info_menu == 6:
			cert = str(input('Tem certeza que deseja fechar o programa? se você não salvou as informações, elas serão perdidas - [S/N]: ')).strip().upper()[0]
			if cert == 'N':
				print(cor('VERDE'), '<<<Programa encerrado!>>>', cor('BRANCO'))
				break
			elif cert == 'S':
				clear()
				continue
		elif info_menu == 4:
			for num in informacoes:
				if num == 0:
					print('Nada ainda')
				else:
					masculino(informacoes)
		elif info_menu == 2:
			clear()
			style_txt('Cadastros')
			with open('Cadastros.txt', 'r') as arquivo:
				print(arquivo.read())
			linha()
			input('Pressione "enter" para sair da lista de cadastros!')
			
			
def pede_info():
	cadastros = list()
	cadastros2 = list()
	while True:
		while True:
			clear()
			linha()
			nome = str(input('NOME: ')).strip().upper()
			if nome.isnumeric():
				clear()
				linha()
				print('ERROR: Digite um nome válido!')
			elif nome.isalpha():
				clear()
				linha()
				break
		idade = int(input('IDADE: '))
		sexo = str(input('SEXO [M/F]: ')).strip().upper()			
		linha()
		salvar(cadastros, nome, idade, sexo)
		cadastros2.append(cadastros[:])
		outro_cadastro = str(input('Deseja cadastrar outra pessoa? ')).strip().upper()
		if outro_cadastro == 'SIM':
			cadastros.clear()
			continue
		else:
			cadastros.clear()
			clear()
			break
	return cadastros2
	