#!/bin/python3.9
# --------------------enivrez-vous-------------------------#
from cryptography.fernet import Fernet
from key import keyGenerator
import os
import shutil
import datetime
import sys


class Cryptonita:
    """Classe que criptografa ou descriptografa os itens, a vosso modo..."""
    def __init__(self, nomeArquivo):
        self.nomeArquivo = nomeArquivo

    def encrypt(self):
        """Criptografa o arquivo"""
        key = keyGenerator()
        # abre a chave:
        with open('/home/marcus/PycharmProjects/criptografa_arquivos/Scripts/key.txt', 'rb') as keey:
            keey.readlines()  # salva a chave
        cifra = Fernet(key)  # define o objeto cifra
        # vai para o diretório local
        os.chdir('/home/marcus/PycharmProjects/criptografa_arquivos/Scripts')

        # copia os arquivos
        shutil.copy2(self.nomeArquivo, f'./{self.nomeArquivo}.crypt')  # cria uma copia, dps remove e deixa msg
        with open(f"{self.nomeArquivo}.crypt", 'rb') as file:
            arquivo = file.read()
        criptografa = cifra.encrypt(arquivo)  # criptografa os arquivos
        print('Arquivos criptografados')

        with open(f"{self.nomeArquivo}.crypt", 'wb') as crypt_file:
            crypt_file.write(criptografa)
            os.remove(self.nomeArquivo)
            with open('read.log', 'a') as leia:
                ler = leia.write(f'O arquivo {self.nomeArquivo} foi criptografado em {datetime.datetime.now()}')
                ler2 = leia.write('\n')
    
    def decrypt(self):
        """ descriptografa o arquivo """
        with open('key.txt', 'rb') as f:
            chave = f.read()
        cifra = Fernet(chave)
        os.chdir('/home/marcus/PycharmProjects/criptografa_arquivos/Scripts') # vai para o diretório atual
        # copia os arquivos
        shutil.copy2(self.nomeArquivo, f'./{self.nomeArquivo}.decrypt')  # cria uma copia, dps remove e deixa msg
        with open(f"{self.nomeArquivo}.decrypt", 'rb') as f:
            arquivo = f.read()
        descriptografa = cifra.decrypt(arquivo)
        print('Arquivo descriptografado')

        with open(f"{self.nomeArquivo}.decrypt", 'wb') as decrypt_file:
            decrypt_file.write(descriptografa)
            with open('read.log', 'a') as leia:
                ler = leia.write(f'O arquivo {self.nomeArquivo} foi descriptografado em {datetime.datetime.now()}')
                ler2 = leia.write('\n')


if __name__ == '__main__':
    print("*************Cryptonita************")
    print("""             

          .,------------,.
        //   =^^^^^^^\__| \\
        \\\   `------.   .//
         `\\`--...._  `;//'
           `\\.-,___;.//'
             `\\-..-//'
               `\\//'

         """"")
    print('************************************')
    arquivo = str(input('Nome do arquivo a ser manipulado: '))
    crypto = Cryptonita(arquivo)
    # escolha
    try:
        escolha: int = int(input('Por favor, digite:\n1-Para criptografar\n2-Para descriptografar\n'))
    except ValueError or TypeError:
        print('Opção não reconhecida\nNada foi alterado.')
        sys.exit(1)
    else:
        if escolha == 1:
            crypto.encrypt()
        elif escolha == 2:
            crypto.decrypt()
        else:
            print('Opção inválida')
