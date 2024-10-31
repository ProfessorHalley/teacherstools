import os
import hashlib
from collections import defaultdict

def calcular_hash_arquivo(caminho_arquivo, algoritmo="sha256"):
    """Calcula o hash de um arquivo usando o algoritmo especificado."""
    hash_algoritmo = hashlib.new(algoritmo)
    with open(caminho_arquivo, "rb") as arquivo:
        while True:
            bloco = arquivo.read(4096)
            if not bloco:
                break
            hash_algoritmo.update(bloco)
    return hash_algoritmo.hexdigest()

def verificar_arquivos_duplicados(diretorio):
    """Verifica arquivos duplicados em um diretório, com base em seus hashes."""
    hash_para_arquivos = defaultdict(list)
    
    # Calcula o hash de cada arquivo no diretório
    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        
        # Verifica se é um arquivo
        if os.path.isfile(caminho_arquivo):
            hash_arquivo = calcular_hash_arquivo(caminho_arquivo)
            hash_para_arquivos[hash_arquivo].append(nome_arquivo)
    
    # Exibe arquivos duplicados
    arquivos_duplicados = {hash: arquivos for hash, arquivos in hash_para_arquivos.items() if len(arquivos) > 1}
    
    if arquivos_duplicados:
        print("Arquivos duplicados encontrados:")
        for hash, arquivos in arquivos_duplicados.items():
            print(f"Hash: {hash}")
            print("Arquivos:", arquivos)
    else:
        print("Nenhum arquivo duplicado encontrado.")

# Caminho para o diretório onde os arquivos estão armazenados
diretorio = "./folder"  # Substitua pelo caminho da pasta onde estão os arquivos
verificar_arquivos_duplicados(diretorio)
