def bit_to_int(lista):
   result = 0
   count = 0
   potencia = 2;

   for x in reversed(lista):
     if(x==1):
       result = result + potencia**count
     count+=1
   return result

def int_to_bit(numero):
  listaBit = [1 if digit=='1' else 0 for digit in bin(numero)[2:]] #essa funcao retorna algo com 0b11 para 3, o [2:] pega depois do segundo elemento e retorna somente 11
  if len(listaBit)==0:
    listaBit = [0,0,0,0, 0, 0, 0, 0]
  elif len(listaBit)==1:
    listaBit = [0,0,0, 0, 0, 0, 0] + listaBit
  elif len(listaBit)==2:
    listaBit = [0,0, 0, 0, 0, 0] + listaBit
  elif len(listaBit)==3:
    listaBit = [0, 0, 0, 0, 0] + listaBit
  elif len(listaBit)==4:
    listaBit = [0, 0, 0, 0] + listaBit
  elif len(listaBit)==5:
    listaBit = [0,0,0] + listaBit
  elif len(listaBit)==6:
    listaBit = [0,0] + listaBit
  elif len(listaBit)==7:
    listaBit = [0] + listaBit

  return listaBit

	#o 1 if eh para converter de char pra int

def xor(lista1, lista2):
  listaResultado=[]
  for i in range(len(lista1)):
    listaResultado = listaResultado + [lista1[i]^lista2[i]]
  return listaResultado

def binvalue(val, bitsize): #Return the binary value as a string of the given size 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval

def string_to_bit_array(text):#Convert a string into a list of bits
    array = list()
    for char in text:
        binval = binvalue(char, 8)#Get the char value on one byte
        array.extend([int(x) for x in list(binval)]) #Add the bits to the final list
    return array

def nsplit(s, n):#Split a list into sublists of size "n"
    return [s[k:k+n] for k in xrange(0, len(s), n)]

def bit_array_to_string(array): #Recreate the string from the bit array
    res = ''.join([chr(int(y,2)) for y in [''.join([str(x) for x in bytes]) for bytes in  nsplit(array,8)]])   

    return res
def  separabytes (lista):
    listaFinal = []
    a=0
    b=8
    for x in range(1,17):
     listaFinal.append(lista[a:b])
     a=a+8
     b=b+8
    return listaFinal

def juntaBits (lista):
    listaFinal = []
    for x in xrange(0,16):
        listaFinal = listaFinal + lista[x]
    return listaFinal