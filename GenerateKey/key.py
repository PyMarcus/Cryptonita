from cryptography.fernet import Fernet



def keyGenerator():
    # # salva a chave gerada no arquivo, por precaução
    chave = Fernet.generate_key()
    with open('key.txt', 'w') as f:
        f.writelines(str(chave.decode()))
    return chave