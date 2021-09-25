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
    aux=[]
    if(modulo==27):
        for i in range(0,len(palabra)):
            if(i>=30):
                y = (alfabetoLetras.get(palabra[i]) - alfabetoLetras.get(aux[i-30])) % 27
                if(y>26):
                    y=y+27
                x.append(alfabetoNumero.get(y))
                aux.append(alfabetoNumero.get(y))
            else:
                y = (alfabetoLetras.get(palabra[i]) - alfabetoLetras.get(clave[i])) % 27
                if(y>26):
                    y=y+27
                x.append(alfabetoNumero.get(y))
                aux.append(alfabetoNumero.get(y))
    
    return x


palabra="XHGDQESDMPKÑDEEDKNGJZPFJSUIFZOLFCINFJCESVZTGBFXCIUDAYNUUDIZYWWZBEYNVQWIVUNKZEPHDODQUZZLBDNDRWTHQSERÑIVMLERCMGIFLSORZXTSDIGLOXQSDJHWVCIWQXQJCKMBPOKMPSKMUVIMNJDNBLCSZHXHNYYUIXDBSOXHZLXWVGDJGXHWLTDWKÑSAQIMZLNBVMLXHUOQQXIQGWGUFTWKZKMOKUDNINSIFJDUOZIJBSVVOWFAIEÑGYOWPSOAP"
clave="UNODELOSMASGRANDESCRIPTOGRAFOS"

modulo = 27
key=generar(palabra,clave)
#print(palabra)
#print(key)
cifrar_texto=cifrar(palabra,key,27)
print(cifrar_texto)


st = ""
for x in cifrar_texto:
    st += x
print(st)







