import sys #Passagem de parametros
#Importacao das bibliotecas
from  Bibliotecas.file import * 
from  Bibliotecas.manipulaBloco import * 
from  Bibliotecas.geradorChavesDES import *  
from  Bibliotecas.binario import *
from  Bibliotecas.matrizes_Sboxes import * 


if(len(sys.argv)<5):
  print "ERRO: Passe todos parametros corretamente!"
  print "\t Nome do arquivo de entrada"
  print "\t Nome do arquivo de saida"
  print "\t Nome do arquivo com chave de Criptografia/Decriptografia"
  print "\t Digite o codigo:"
  print "\t\t0 - Criptografar"
  print "\t\t1 - Decriptografar"
  exit()


#1 e 2 pq o 0 eh o nome do arquivo do codigo
pathArquivo = sys.argv[1]
pathArquivoSaida = sys.argv[2]
pathArquivoChave = sys.argv[3]
acao = sys.argv[4]
if((acao!='0') and (acao!='1')):
  print "ERRO: Passe todos parametros corretamente!"
  print "\t Nome do arquivo de entrada"
  print "\t Nome do arquivo de saida"
  print "\t Nome do arquivo com chave de Criptografia/Decriptografia"
  print "\t Digite o codigo:"
  print "\t\t0 - Criptografar"
  print "\t\t1 - Decriptografar"
  print "N"
  exit()

#Realiza leitura do arquivo e coloca na variavel buffer
buffer = leArquivo(pathArquivo)
#print pathArquivoChave
chave = str((leArquivo(pathArquivoChave)))

#Converte a leitura para um array de Bits (o que ta no arquivo eh interpretado como string e depois convertido para bit, nao precisa ser necessariamente uma string, funciona com outros arquivos tbm)
arquivoCompletoEmBits=string_to_bit_array(buffer)

print "Tamanho do arquivo: " + str(len(arquivoCompletoEmBits)) + " bits."

arquivoFinal = []

if(acao=='0'):
  listaChaves = geraSubChaves(chave)
else:
  listaChaves = geraSubChavesOrdemInversa(chave)

#---------------------DES---------------------#

#Preenche o que falta com zeros
if((len(arquivoCompletoEmBits)%64)!=0):
  listaZeros = []
  for f in range(64-len(arquivoCompletoEmBits)%64):
    listaZeros = listaZeros + [0]
  arquivoCompletoEmBits = arquivoCompletoEmBits + listaZeros


#Executa criptografia ou decriptografia em cada bloco de 64 bits
for i in range (len(arquivoCompletoEmBits)/64):
  inicio = i*64
  fim = (i+1)*64

  #Separa um bloco/buffer de 64 bits do total para encriptar
  bloco = separaBloco(arquivoCompletoEmBits, inicio, fim)
 
  #Permuta bloco usando matriz/vetor de permutacao
  blocoPermutado = permutaBloco(bloco, IPI)
  #Separa em L e R
  L, R = separaBlocoLR(blocoPermutado)

  #Gera uma subchave (ainda nao eh o final)
  #if acao == 0, geraordem normal, se 1 inverte ,,,isso vai decriptar ou encriptar

  for m in range(16):

    #------------------FUNCAO F------------------------#
    #Expande bloco R
    blocoExpandido = expandeBloco(R, E)
    subChave = listaChaves[m]
    #print len(subChave)
    #exit()

    #Faz xor do bloco R expandido com subChave da rodada
    resultadoXOR = xor(blocoExpandido, subChave)

    #Divide resultado do xor com a chave em grupos de 6 bits para passar pelo S_BOX
    listaSepara = divide6bits(resultadoXOR)
    #print listaSepara
    countSbox = 0
    listaAposSbox = []

    #Com o S_BOX ha a substituicao de alguns digitos, esses digitos sao definidos de acordo com a linha e coluna...que sao definidas
    #com base nos bits do numero... o bit mais significativo concatenado com o menos significativo resulta no numero da linha
    #o resto que sobrar eh o numero da coluna
    for l in listaSepara:
      #Concatena primeiro bit com ultimo
      linhaBinario = [l[0]] + [l[len(l)-1]]
      #Transforma para inteiro
      linhaInt = bit_to_int(linhaBinario)

      #Com os bits que sobraram descobre-se a coluna
      colunaBinario = l[1:len(l)-1] # len(l)-1 pq o intervalo eh fechado, se fosse len(l) pegaria o ultimo tbm
      colunaInt = bit_to_int(colunaBinario)

      #print (S_BOX[countSbox][linhaInt][colunaInt])
      #countSbox determina qual Sbox sera usada (varia de 0 a 7) e linhaInt e linhaColuna a linha e a coluna dessa S_box
      modificado = int_to_bit(S_BOX[countSbox][linhaInt][colunaInt])

      #Copia esses 6 bits (agora 4) para a listaFinal
      listaAposSbox = listaAposSbox + modificado[:]
      countSbox+=1

    #Realiza permutacao na listaAposSbox antes de sair da funcao F....

    finalAposFuncaoF = permutaBloco(listaAposSbox, PF)

    #------------------FIM FUNCAO F------------------------#

    aux = R[:]
    R = xor(finalAposFuncaoF, L)
    L = aux

  blocoFinal = R + L

  #Ultima permutacao
  blocoPermutadoFinal = permutaBloco(blocoFinal, IPI_1)
  arquivoFinal = arquivoFinal + blocoPermutadoFinal

try:
    arqfinal = open(pathArquivoSaida,"wb")
except IOError:
    print "Erro ao abrir o arquivo"
arqfinal.write(bit_array_to_string(arquivoFinal))

arqfinal.close()
print "Completo!"