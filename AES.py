#Importacao das bibliotecas
import sys #Passagem de parametros
#Importacao das bibliotecas
from  Bibliotecas.file import * 
from  Bibliotecas.manipulaBloco import * 
from  Bibliotecas.geradorChavesAES import *  
from  Bibliotecas.binario import * 
from  Bibliotecas.matrizes_Sboxes import * 

def substituicaoBytes (lista):
    for x in xrange(0,16):
        lista[x]= string_to_bit_array(chr(Sbox[bit_to_int(lista[x][0:4])][bit_to_int(lista[x][4:8])]))
        
def inversaoSubstituicaoBytes (lista):
    for x in xrange(0,16):
        lista[x]= string_to_bit_array(chr(InvSbox[bit_to_int(lista[x][0:4])][bit_to_int(lista[x][4:8])]))


def deslocamentoLinhas (lista):
    lista[4],lista[5],lista[6],lista[7]= lista[5],lista[6],lista[7],lista[4]
    lista[8],lista[9],lista[10],lista[11]= lista[10],lista[11],lista[8],lista[9]
    lista[12],lista[13],lista[14],lista[15]= lista[15],lista[12],lista[13],lista[14]

def inversaoDeslocamentoLinhas (lista):
    lista[4],lista[5],lista[6],lista[7]= lista[7],lista[4],lista[5],lista[6]
    lista[8],lista[9],lista[10],lista[11]= lista[10],lista[11],lista[8],lista[9]
    lista[12],lista[13],lista[14],lista[15]= lista[13],lista[14],lista[15],lista[12]


def adicaoChave (b,c):
    for x in xrange(0,16):
        b[x] =  xor(b[x],c[x])
    return b

def mixColunas (lista):
    c= lista[:]
    
    c[0] = int_to_bit(g2[(bit_to_int(lista[0]))] ^ g3[(bit_to_int(lista[4]))] ^ bit_to_int(lista[8]) ^ bit_to_int(lista[12]))
    c[4] = int_to_bit(bit_to_int(lista[0]) ^ g2[(bit_to_int(lista[4]))] ^g3[(bit_to_int(lista[8]))] ^ bit_to_int(lista[12]))
    c[8] = int_to_bit(bit_to_int(lista[0]) ^ bit_to_int(lista[4]) ^ g2[(bit_to_int(lista[8]))] ^ g3[(bit_to_int(lista[12]))])
    c[12] = int_to_bit(g3[(bit_to_int(lista[0]))] ^ bit_to_int(lista[4]) ^ bit_to_int(lista[8]) ^ g2[(bit_to_int(lista[12]))])


    c[1] = int_to_bit(g2[(bit_to_int(lista[1]))] ^ g3[(bit_to_int(lista[5]))] ^ bit_to_int(lista[9]) ^ bit_to_int(lista[13]))
    c[5] = int_to_bit(bit_to_int(lista[1]) ^ g2[(bit_to_int(lista[5]))] ^g3[(bit_to_int(lista[9]))] ^ bit_to_int(lista[13]))
    c[9] = int_to_bit(bit_to_int(lista[1]) ^ bit_to_int(lista[5]) ^ g2[(bit_to_int(lista[9]))] ^ g3[(bit_to_int(lista[13]))])
    c[13] = int_to_bit(g3[(bit_to_int(lista[1]))] ^ bit_to_int(lista[5]) ^ bit_to_int(lista[9]) ^ g2[(bit_to_int(lista[13]))])

    c[2] = int_to_bit(g2[(bit_to_int(lista[2]))] ^ g3[(bit_to_int(lista[6]))] ^ bit_to_int(lista[10]) ^ bit_to_int(lista[14]))
    c[6] = int_to_bit(bit_to_int(lista[2]) ^ g2[(bit_to_int(lista[6]))] ^g3[(bit_to_int(lista[10]))] ^ bit_to_int(lista[14]))
    c[10] = int_to_bit(bit_to_int(lista[2]) ^ bit_to_int(lista[6]) ^ g2[(bit_to_int(lista[10]))] ^ g3[(bit_to_int(lista[14]))])
    c[14] = int_to_bit(g3[(bit_to_int(lista[2]))] ^ bit_to_int(lista[6]) ^ bit_to_int(lista[10]) ^ g2[(bit_to_int(lista[14]))])

    c[3] = int_to_bit(g2[(bit_to_int(lista[3]))] ^ g3[(bit_to_int(lista[7]))] ^ bit_to_int(lista[11]) ^ bit_to_int(lista[15]))
    c[7] = int_to_bit(bit_to_int(lista[3]) ^ g2[(bit_to_int(lista[7]))] ^g3[(bit_to_int(lista[11]))] ^ bit_to_int(lista[15]))
    c[11] = int_to_bit(bit_to_int(lista[3]) ^ bit_to_int(lista[7]) ^ g2[(bit_to_int(lista[11]))] ^ g3[(bit_to_int(lista[15]))])
    c[15] = int_to_bit(g3[(bit_to_int(lista[3]))] ^ bit_to_int(lista[7]) ^ bit_to_int(lista[11]) ^ g2[(bit_to_int(lista[15]))])
    
    return c
  
def inversoMixColunas (lista):
    c= lista[:]

    c[0] = int_to_bit(g14[(bit_to_int(lista[0]))] ^ g11[(bit_to_int(lista[4]))] ^ g13[(bit_to_int(lista[8]))] ^g9[(bit_to_int(lista[12]))])
    c[4] = int_to_bit(g9[(bit_to_int(lista[0]))] ^ g14[(bit_to_int(lista[4]))] ^ g11[(bit_to_int(lista[8]))] ^ g13[(bit_to_int(lista[12]))])
    c[8] = int_to_bit(g13[(bit_to_int(lista[0]))] ^ g9[(bit_to_int(lista[4]))] ^ g14[(bit_to_int(lista[8]))] ^ g11[(bit_to_int(lista[12]))])
    c[12] = int_to_bit(g11[(bit_to_int(lista[0]))] ^ g13[(bit_to_int(lista[4]))] ^ g9[(bit_to_int(lista[8]))] ^ g14[(bit_to_int(lista[12]))])

    c[1] = int_to_bit(g14[(bit_to_int(lista[1]))] ^ g11[(bit_to_int(lista[5]))] ^ g13[(bit_to_int(lista[9]))] ^g9[(bit_to_int(lista[13]))])
    c[5] = int_to_bit(g9[(bit_to_int(lista[1]))] ^ g14[(bit_to_int(lista[5]))] ^ g11[(bit_to_int(lista[9]))] ^ g13[(bit_to_int(lista[13]))])
    c[9] = int_to_bit(g13[(bit_to_int(lista[1]))] ^ g9[(bit_to_int(lista[5]))] ^ g14[(bit_to_int(lista[9]))] ^ g11[(bit_to_int(lista[13]))])
    c[13] = int_to_bit(g11[(bit_to_int(lista[1]))] ^ g13[(bit_to_int(lista[5]))] ^ g9[(bit_to_int(lista[9]))] ^ g14[(bit_to_int(lista[13]))])

    c[2] = int_to_bit(g14[(bit_to_int(lista[2]))] ^ g11[(bit_to_int(lista[6]))] ^ g13[(bit_to_int(lista[10]))] ^g9[(bit_to_int(lista[14]))])
    c[6] = int_to_bit(g9[(bit_to_int(lista[2]))] ^ g14[(bit_to_int(lista[6]))] ^ g11[(bit_to_int(lista[10]))] ^ g13[(bit_to_int(lista[14]))])
    c[10] = int_to_bit(g13[(bit_to_int(lista[2]))] ^ g9[(bit_to_int(lista[6]))] ^ g14[(bit_to_int(lista[10]))] ^ g11[(bit_to_int(lista[14]))])
    c[14] = int_to_bit(g11[(bit_to_int(lista[2]))] ^ g13[(bit_to_int(lista[6]))] ^ g9[(bit_to_int(lista[10]))] ^ g14[(bit_to_int(lista[14]))])

    c[3] = int_to_bit(g14[(bit_to_int(lista[3]))] ^ g11[(bit_to_int(lista[7]))] ^ g13[(bit_to_int(lista[11]))] ^g9[(bit_to_int(lista[15]))])
    c[7] = int_to_bit(g9[(bit_to_int(lista[3]))] ^ g14[(bit_to_int(lista[7]))] ^ g11[(bit_to_int(lista[11]))] ^ g13[(bit_to_int(lista[15]))])
    c[11] = int_to_bit(g13[(bit_to_int(lista[3]))] ^ g9[(bit_to_int(lista[7]))] ^ g14[(bit_to_int(lista[11]))] ^ g11[(bit_to_int(lista[15]))])
    c[15] = int_to_bit(g11[(bit_to_int(lista[3]))] ^ g13[(bit_to_int(lista[7]))] ^ g9[(bit_to_int(lista[11]))] ^ g14[(bit_to_int(lista[15]))])

    return c


def encripta (buffer, pathArquivoSaida, chave):
    #Leitura Arquivo e tranforma em binario e quebra em cadeia de 8 bits.
    cadeiaBit = string_to_bit_array(buffer)

    print "Tamanho do arquivo: " + str(len(cadeiaBit)) + " bits."

    #Preenche o que falta com zeros
    if((len(cadeiaBit)%128)!=0):
      listaZeros = []
      for f in range(128-len(cadeiaBit)%128):
        listaZeros = listaZeros + [0]
      cadeiaBit = cadeiaBit + listaZeros

    textoEncriptado = []


    listaChaves = keyExpansion(chave)


    #Executa criptografia ou decriptografia em cada bloco de 64 bits
    for i in range (len(cadeiaBit)/128):
        
        inicio = i*128
        fim = (i+1)*128

        bloco = separaBloco(cadeiaBit, inicio, fim)
        bloco = separabytes(bloco)

        #Inicio da encriptacao
        chave1 = separabytes(listaChaves[0])
        bloco = adicaoChave(bloco,chave1)

        for x in xrange(1,10):
            substituicaoBytes (bloco)
            deslocamentoLinhas (bloco)
            bloco = mixColunas(bloco)
            chave1 = separabytes(listaChaves[x])
            bloco =  adicaoChave(bloco,chave1)

        substituicaoBytes (bloco)
        deslocamentoLinhas (bloco)
        chave1 = separabytes(listaChaves[10])
        bloco =  adicaoChave(bloco,chave1)

        #Junta Bits e tranforma em string
        bloco = juntaBits (bloco)
        textoEncriptado = textoEncriptado + bloco 


    arqfinal = open(pathArquivoSaida,"wb")
    arqfinal.write(bit_array_to_string(textoEncriptado))
    arqfinal.close()

    

    
def decripta (buffer, pathArquivoSaida, chave):


  #Leitura Arquivo e tranforma em binario e quebra em cadeia de 8 bits.
  cadeiaBit = string_to_bit_array(buffer)

  print "Tamanho do arquivo: " + str(len(cadeiaBit)) + " bits."

  #Preenche o que falta com zeros
  if((len(cadeiaBit)%128)!=0):
    listaZeros = []
    for f in range(128-len(cadeiaBit)%128):
      listaZeros = listaZeros + [0]
    cadeiaBit = cadeiaBit + listaZeros


  listaChaves = keyExpansion(chave)
  listaChaves.reverse()

  textoClaro = []

  for i in range (len(cadeiaBit)/128):

    inicio = i*128
    fim = (i+1)*128

    bloco = separaBloco(cadeiaBit, inicio, fim)
    bloco = separabytes(bloco)
    
    # Leitura da Chave Fixa e tranforma em binario e quebra em cadeia de 8 bits.
      

    #Inicio da descriptacao
    chave1 = separabytes(listaChaves[0])
    bloco =  adicaoChave(bloco,chave1)
    inversaoDeslocamentoLinhas (bloco)
    inversaoSubstituicaoBytes (bloco)

    for x in xrange(1,10):
        chave1 = separabytes(listaChaves[x])
        bloco =  adicaoChave(bloco,chave1)
        bloco = inversoMixColunas(bloco)
        inversaoDeslocamentoLinhas (bloco)
        inversaoSubstituicaoBytes (bloco)

    chave1 = separabytes(listaChaves[10])
    bloco =  adicaoChave(bloco,chave1)
    #printMatriz(bloco)
    #Junta Bits e tranforma em string
    bloco = juntaBits (bloco)


    textoClaro = textoClaro + bloco 

  arqfinal = open(pathArquivoSaida,"wb")
  arqfinal.write(bit_array_to_string(textoClaro))
  arqfinal.close()


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

buffer = leArquivo(pathArquivo)
chave = leArquivo(pathArquivoChave)
chave = string_to_bit_array(chave)
#print chave

if(acao=='0'):
    encripta(buffer, pathArquivoSaida, chave)
else:
    decripta(buffer, pathArquivoSaida, chave)
print "Completo!"