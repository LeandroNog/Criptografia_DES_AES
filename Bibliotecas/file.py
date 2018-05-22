def leArquivo(nome):
	try:
		arquivo = open(nome,"rb")
	except IOError:
		print "Erro ao abrir o arquivo"
	arquivo.seek(0,2)
	tamanho = arquivo.tell()
	arquivo.seek(0)
	buffer = arquivo.read(tamanho)
	arquivo.close()
	return buffer