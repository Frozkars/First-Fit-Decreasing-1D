import numpy as np
c=int(input("Digite o comprimento dos conteiners: "))
x=1
i=1
vetor = []

while x!=0:
    x = float(input("Digite o comprimento do objeto %i  [Para terminar, digite 0]: " %i))
    if x!=0:
        vetor.append(x)
    i+=1

n=i-1
V = sorted(vetor)
V.reverse()

def criar_container(vetor,c,n):
    container = []
    restantes = []
    for j in vetor:
        if (sum(container)+j)<= c:
            container.append(j)
        else:
            restantes.append(j)

    return container, restantes

def criar_conjunto(vetor,c,n):
    C=[]
    C.append(criar_container(vetor,c,n)[0])
    restantes=criar_container(vetor,c,n)[1]
    while (restantes != []):
        y=criar_container(restantes,c,n)[0]
        restantes = criar_container(restantes,c,n)[1]
        C.append(y)

    return C

C = criar_conjunto(V,c,n)
qntd_cont=len(C)
desperdicio_total=0
for z in range(qntd_cont):
    desperdicio=c-sum(C[z])
    desperdicio_total+=desperdicio
    print("Conteiner "+str(z+1)+": "+str(np.array(C[z]))+" - Desperdicio: %.2f" %(desperdicio))
print("Desperdicio total: %.2f"%desperdicio_total)