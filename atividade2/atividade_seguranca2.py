import re
import math
   
def encript(chave, md): #md=mensagem decifrada
    frase=''
    matriz = formarMatrizParaEncript(md, chave)
    matriz.sort() 
    for l in matriz:
        del l[0]
        for c in l:
            frase+=c
        frase+=" "
    return re.sub('\s{2,}', " ",frase)
    
    
def formarMatrizParaEncript(m, chave):
    m = chave + m.replace(" ", "")
    palavra = []
    matriz = []
    tamanhoChave = len(chave)
    tamanhoM = len(m)
    
    while tamanhoM % tamanhoChave!=0:
        m+=" "
        tamanhoM = len(m)
    
    for i in range(tamanhoChave):
        for j in range(int(tamanhoM / tamanhoChave)):
            palavra.append(m[j * tamanhoChave + i]) # j * tamanhoChave + i = calculo para simular uma matriz    
        
        matriz.append(palavra)
        palavra = []
        
    return matriz



def descript(chave, me):
    chaveList = [k for k in chave if k!=" "]
    meMatriz = formarMatrizParaDescript(me, chaveList)
    del me
    me = []
    for l in chave:
        linha = [k[1:] for k in meMatriz if k[0]==l]
        me.append([k for k in linha[0]])
    
    frase = ""
    while len(me[0])!=0:
        for i in range(len(me)):
            if(me[i]!=[]):
                frase+=me[i][0]
                del me[i][0]
    
    return frase
    
def formarMatrizParaDescript(m, chave):
    m = m.split(" ")
    copiaChave = chave[0:]
    copiaChave.sort()
    matriz = []
    
    for linha, letraChave in zip(m, copiaChave):
        matriz.append([v for v in letraChave+linha])
    
    return matriz
    
    
frase1 = encript("zebras", "teste 123 Aaa")
frase2 = descript("zebras", frase1)
print(frase1)
print(frase2)
