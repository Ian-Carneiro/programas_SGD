alf = "abcdefghijklmnopqrstuvwxyz1234567890"

def cifrar(key, msg):
    msgCifrada = ""
    for letra in msg:
        if letra==" ":
            msgCifrada+=letra
        else:
            posAlf = alf.index(letra)+key
            if posAlf > len(alf)-1:
                posAlf = (posAlf%(len(alf)-1))-1
            msgCifrada += alf[posAlf]
    return msgCifrada

def decifrar(key, msg):
    msgDecifrada = ""
    for letra in msg:
        if letra==" ":
            msgDecifrada+=letra
        else:
            posAlf = alf.index(letra)-key
            msgDecifrada += alf[posAlf]
    return msgDecifrada
    
msg1 = cifrar(10, "hello world123")
msg2 = decifrar(10, msg1)

print(msg1)
print(msg2)
