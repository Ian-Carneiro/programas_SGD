import codecs
import time

tic = time.time()#tempo de inicio do programa
'''
Para o rc4 é necessário gerar a keystream atravez de uma semente(que será a chave para criptografar
e descriptografar).
'''
def ksa(key):
    s = [k for k in range(256)]
    j = 0
    for i in range(256):
        j = (j + s[i] + ord(key[i%len(key)])) % 256
        aux = s[i]
        s[i] = s[j]
        s[j] = aux
    return s

'''
    Logo depois é necessário que o resutado do embaralhamento de um array, com números de 0 a 255, tenha o mesmo 
tamanho da mensagem. Feito estes dois métodos a keystream estará embaralhada pelo algorítmo através
do tamanho da mensagem e da chave inicial que foi dada.
'''
def prga(msg, s):
    i = 0
    j = 0
    k = []
    for msgLen in range(len(msg),0,-1):
        i = (i+1)%256
        j = (j+s[i])%256
        aux = s[i]
        s[i] = s[j]
        s[j] = aux
        k.append(s[(s[i]+s[j])%256])
    return k

'''
KEYSTREAM
'''
def keystream(key, msg):
    s = ksa(key)
    k = prga(msg, s)
    return k

'''
    De posse da keystream é posivel agora a cifragem da mensagem utilizando a soma de cada bit da chave com
cada bit da mensagem(utilizando o operador xor ^).
'''
def rc4(key, msg):
    keyS = keystream(key, msg)
    msg2 = []
    for c in range(len(msg)):
        msg2.append(ord(msg[c])^keyS[c])
    msg = [chr(c) for c in msg2]
    return "".join(msg)

'''
    Os metódos encrypt() e decrypt() servem respectivamente para: transformar a mensagem encriptada(que até 
então é composta de caracteres da tabela acii) em um valor hexadecimal e transformar o parâmetro "msg", da
função rc4, em valores da tabela ascii. 
'''
def encrypt(key, msg):
    encr = rc4(key, msg)
    return encr.encode('utf-8').hex()
    
def decrypt(key, msg):
    return rc4(key, bytes.fromhex(msg).decode("utf-8"))

'''
    Aqui é feito um teste de encriptação e decriptação do endereço do IFPB de Cajazeiras e o tempo total de 
execução do algoritmo.
'''
e = encrypt("KEY", "147, R. José Antônio da, R. José Leôncio da Silva, 300 - Lot. Jardim Oasis, Cajazeiras - PB, 58900-000")
d = decrypt("KEY", e)

tac = time.time()#tempo de fim do programa

print("Encriptada: "+e, end="\n\n")
print("Decriptada: "+d, end="\n\n")
print("Tempo de execução: "+str((tac-tic)*1000)+" ms")
