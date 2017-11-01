import numpy as np

c=int(input("Digite o comprimento dos contêiners: "))
n=int(input("Digite a quantidade de objetos à serem alocados: "))

def criar_vetor(n):
    vetor = []
    for i in range(n):
        if n==1:
            x = int(input("Digite o comprimento do objeto: "))
        else:
            x = int(input("Digite o comprimento do %iº objeto: " %(i+1)))
        vetor.append(x)
    return vetor

V = criar_vetor(n)
V1 = sorted(V)
V1.reverse()

def criar_conjunto(vetor,c,n):
    conjunto = []
    conteiner = []
    for j in range(n):
        for k in conjunto:
            if (sum(k)+vetor[j])<= c:
                conteiner.append(j)
            else:
                conjunto.append(conteiner)
    return conjunto

C = criar_conjunto(V1,c,n)
print(C)
