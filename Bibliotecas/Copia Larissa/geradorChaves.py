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
   return  chave1[len(chave1)-y:]+ chave1[:len(chave1)-1]

print("Criptografia")
chaveInicial= "hlkjasdf";
k=string_to_bit_array(chaveInicial)
chaveIntermediaria=permutacao_CP1(k)
ladoL=criaL(chaveIntermediaria)
ladoR=criaR(chaveIntermediaria)




for i in range(1,17):
	
	if((i==1)or(i==2)or(i==9)or(i==16)):
		ladoR=rotacionaEsquerda(ladoR,1)
		ladoL=rotacionaEsquerda(ladoL,1)
		aux=ladoL+ladoR
		chaveK=permutacao_CP2(aux)
		print(chaveK)

		
	else:
		ladoR=rotacionaEsquerda(ladoR,2)
		ladoL=rotacionaEsquerda(ladoL,2)
		aux=ladoL+ladoR
		chaveK=permutacao_CP2(aux)
		print(chaveK)

		


print("Descriptografia")
chaveIntermediaria=permutacao_CP1(k)
ladoL=criaL(chaveIntermediaria)
ladoR=criaR(chaveIntermediaria)
for i in range(1,17):
	if((i==1)or(i==2)or(i==9)or(i==16)):
		ladoR=rotacionaDireita(ladoR,1)
		ladoL=rotacionaDireita(ladoL,1)
		aux=ladoL+ladoR
		chaveK=permutacao_CP2(aux)
		print(chaveK)

	else:
		ladoR=rotacionaDireita(ladoR,1)
		ladoR=rotacionaDireita(ladoR,1)
		ladoL=rotacionaDireita(ladoL,1)
		ladoL=rotacionaDireita(ladoL,1)
		aux=ladoL+ladoR
		chaveK=permutacao_CP2(aux)
		print(chaveK)
