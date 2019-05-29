from numpy.linalg import inv
import numpy as np

msg = "DELAYOPERATIONS"
chave = np.array([[8, 6, 9, 5], [6, 9, 5, 10],[5, 8, 4, 9], [10, 6, 11, 4]])
alph = "KPCOHARNGZEYSMWFLVIQDUXBTJ"

def criarMatriz(msg, alph, ordemMatriz):
    msg = msg.replace(" ", "")
    while len(msg)<ordemMatriz**2:
        msg+="U"
    msgMatriz = []
    linha = []
    for i in msg:
        linha.append(alph.index(i))
        if len(linha)==4:
            msgMatriz.append(linha)
            linha = []
    return msgMatriz

def cifrar(msg, alph, chave):
    msgMatriz = criarMatriz(msg, alph, len(chave))
    matrizCod = []
    for lMsg in msgMatriz:
        linha = [] 
        for lChave in chave:
            linha.append(int(sum(np.array(lMsg)*np.array(lChave))%26))
        matrizCod.append(linha)
    return matrizCod

def decifrar(msg, alph, chave):
    chave = inv(chave)%26
    msgMatriz = criarMatriz(msg, alph, len(chave))
    matrizDec = []
    for lMsg in msgMatriz:
        linha = [] 
        for lChave in chave:
            linha.append(int(round(sum(np.array(lMsg)*np.array(lChave))%26)))
        matrizDec.append(linha)
    return matrizDec

def apresentar(matriz, alph):
    s = ""
    for linha in matriz:
        s += "".join([alph[l] for l in linha])
    return s

c = cifrar(msg, alph, chave)
a = apresentar(c, alph)
print(a)
d = decifrar(a, alph, chave)
a = apresentar(d, alph)
print(a)
