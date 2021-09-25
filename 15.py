alfabetoLetras = {
  "A" : 0,
  "B" : 1,
  "C" : 2,
  "D" : 3,
  "E" : 4,
  "F" : 5,
  "G" : 6,
  "H" : 7,
  "I" : 8,
  "J" : 9,
  "K" : 10,
  "L" : 11,
  "M" : 12,
  "N" : 13,
  "Ñ" : 14,
  "O" : 15,
  "P" : 16,
  "Q" : 17,
  "R" : 18,
  "S" : 19,
  "T" : 20,
  "U" : 21,
  "V" : 22,
  "W" : 23,
  "X" : 24,
  "Y" : 25,
  "Z" : 26
}

alfabetoNumero = {
  0: "A",
  1: "B",
  2: "C",
  3: "D",
  4: "E",
  5: "F",
  6: "G",
  7: "H",
  8: "I",
  9: "J",
  10: "K",
  11: "L",
  12: "M",
  13: "N",
  14: "Ñ",
  15: "O",
  16: "P",
  17: "Q",
  18: "R",
  19: "S",
  20: "T",
  21: "U",
  22: "V",
  23: "W",
  24: "X",
  25: "Y",
  26: "Z"
}


def generar(palabra,clave):
    if(len(palabra)>len(clave)):
        clave=list(clave)
        for i in range(0,len(palabra)-len(clave)):
            clave.append(clave[i])
    return("" . join(clave))


def cifrar(palabra,clave,modulo):
    x=[]
    if(modulo==27):
        for i in range(0,len(palabra)):
            y = (alfabetoLetras.get(palabra[i]) - alfabetoLetras.get(clave[i])) % 27
            if(y>26):
                y=y+27
            x.append(y)
    elif(modulo==191):
        for i in range(0,len(palabra)):
            y = (getIndice2(palabra[i]) + getIndice2(clave[i]) -33) % 191
            if(y>190):
                y=y+191
            x.append(y)
    return x
def descifrar(palabra,clave,modulo):
    x=[]

    if(modulo==27):
        for i in range(0,len(palabra)):
            y = (alfabetoLetras.get(palabra[i]) - alfabetoLetras.get(clave[i]))
            if(y>26):
                y=y+27
            x.append(y)
        return x
    elif(modulo==191):
        for i in range(0,len(palabra)):
            y = (getIndice2(palabra[i]) - getIndice2(clave[i]))
            x.append(y)
        return x
def getIndice2(letra):
    return ord(letra)

palabra="WPIXHVYYOSRTECSZBEEGHUUFWRWTZGRWUFSRIWESSXVOHAIHOHWWHCWHUZOBOZEAOYBMCRLTEYOTI"
clave="HIELO"

modulo=int(input("ingrese el modulo :"))
key=generar(palabra,clave)
print(palabra)
print(key)
cifrar_texto=cifrar(palabra,key,modulo)
print(cifrar_texto)
aux_cifrar=[]
if(modulo==27):
    for i in cifrar_texto:
        aux_cifrar.append(alfabetoNumero.get(i))
elif(modulo==191):
    for i in cifrar_texto:
        aux_cifrar.append(chr(i))
print("texto cifrado " ,aux_cifrar)







