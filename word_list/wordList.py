a=['0','1','2','3','4','5','6','7']
b=['a','e','i','o','u']
c=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

paresLetras = []
for consoante in c:
    for vogal in b:
        paresLetras.append(consoante+vogal)

paresNumeros = []
for n1 in a:
    for n2 in a:
        paresNumeros.append(n1+n2)

palavras = []
for parL1 in paresLetras:
    for parL2 in paresLetras:
        for parL3 in paresLetras:
            palavras.append(parL1+parL2+parL3)

keys = []
for palavra in palavras:
    for parNum in paresNumeros:
        keys.append(palavra+parNum+"\n")
txt = open('/home/ian/wl.txt', 'w')
txt.writelines(keys)
txt.close()
print(len(keys))