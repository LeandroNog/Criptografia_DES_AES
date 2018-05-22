from binario import *
from file import *
def permutacao_CP1(chave):
	aux=chave[:56]
	i=0
	cp_1=[57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]
	for x in cp_1:
	    	aux[i]= chave[x-1]
	    	i=i+1
	return aux
def permutacao_CP2(chave):
	aux=chave[:48]
	i=0
	cp_2=[14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

	for x in cp_2:
	    aux[i]= chave[x-1]
	    i=i+1

	return aux

def criaR(chave):
	return chave[len(chave)/2:]

def criaL(chave):
	return chave[:len(chave)/2]

def rotacionaEsquerda(chave,y):
   #Concatena uma lista que comeca na posicao 8 da lista inicial e vai ate o fim, com uma lista
   #que comeca da posicao 0 e vai ate a posicao 7
   return chave[y:] + chave[:y] 
def rotacionaDireita(chave1,y):
   #Concatena uma lista que comeca na posicao 8 da lista inicial e vai ate o fim, com uma lista
   #que comeca da posicao 0 e vai ate a posicao 7
   return  chave1[len(chave1)-y:]+ chave1[:len(chave1)-1] #NAO SERIA Y AQUI??? NO LUGAR DO -1


def geraSubChaves(chave):
	listaChaves = []
	k=string_to_bit_array(chave)
	chaveIntermediaria=permutacao_CP1(k)
	ladoL=criaL(chaveIntermediaria)
	ladoR=criaR(chaveIntermediaria)
	for i in range(1,17):
		if((i==1)or(i==2)or(i==9)or(i==16)):
			ladoR=rotacionaEsquerda(ladoR,1)
			ladoL=rotacionaEsquerda(ladoL,1)
			aux=ladoL+ladoR
		else:
			ladoR=rotacionaEsquerda(ladoR,2)
			ladoL=rotacionaEsquerda(ladoL,2)
			aux=ladoL+ladoR
		chaveK=permutacao_CP2(aux)
		listaChaves = listaChaves + [chaveK]
		#print chaveK
	return listaChaves

def geraSubChavesOrdemInversa(chave):
	listaChaves = []
	k=string_to_bit_array(chave)
	chaveIntermediaria=permutacao_CP1(k)
	ladoL=criaL(chaveIntermediaria)
	ladoR=criaR(chaveIntermediaria)
	for i in range(1,17):
		if(i==1):
			aux=ladoL+ladoR
			
		elif((i==2)or(i==9)or(i==16)):
			ladoR=rotacionaDireita(ladoR,1)
			ladoL=rotacionaDireita(ladoL,1)
			aux=ladoL+ladoR
		else:
			ladoR=rotacionaDireita(ladoR,1)
			ladoR=rotacionaDireita(ladoR,1)
			ladoL=rotacionaDireita(ladoL,1)
			ladoL=rotacionaDireita(ladoL,1)
			aux=ladoL+ladoR
		chaveK=permutacao_CP2(aux)
		#print chaveK
		listaChaves = listaChaves + [chaveK]
	return listaChaves
