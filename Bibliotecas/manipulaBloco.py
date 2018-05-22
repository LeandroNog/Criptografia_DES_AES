def separaBloco(bloco, inicio, fim):
  return bloco[inicio:fim] 

def separaBlocoLR(bloco):
  L = bloco[:32]
  R = bloco[32:]  
  return L, R

def expandeBloco(bloco, matrizE):
	novoBloco = []
  	for x in matrizE:
   		novoBloco = novoBloco + [bloco[x-1]]
	return novoBloco

def permutaBloco(a,IPI):
  aux = []
  for x in IPI:
    aux = aux + [a[x-1]]
  return aux
def desfazPermutacaoBloco(aux, IPI_1):
  aux2 = []
  for x in IPI_1:
    aux2 = [aux[x-1]]
  return aux2

def divide6bits(lista):
  separacao = []
  inicio = 0
  fim = 6
  for i in range(len(lista)/6):
    separacao = separacao + [lista[inicio:fim]]
    inicio = inicio + 6
    fim = fim + 6

  return separacao