Projeto para construção de ferramentas para professores.

1- conferearqduplicado

	1.1- Como Funciona:
 
 Função calcular_hash_arquivo: Calcula o hash de cada arquivo usando o algoritmo SHA-256.
 Função verificar_arquivos_duplicados: Itera sobre cada arquivo na pasta, calcula o hash e armazena em um dicionário, onde a chave é o hash e o valor é uma lista de arquivos com esse hash.
 Identificação de Arquivos Duplicados: Arquivos com o mesmo hash são listados como duplicados, e o script imprime os nomes dos arquivos duplicados.
 
 	1.2 - Executando o Script
  Salve o projeto em sua máquina. O script de verificação é o arquivo verify_copy.py
  Edite a linha diretorio = "/caminho/para/sua/pasta" para apontar para a pasta onde os arquivos estão armazenados.
	
 Execute o script com:
      bash
			
	 python verificar_duplicados.py
Esse script será útil para identificar rapidamente os arquivos duplicados em qualquer pasta.
