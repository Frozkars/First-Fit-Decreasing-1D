c=int(input("Digite o comprimento dos contêiners: "))
x=1
i=1
vetor = []

while x!=0:
    x = int(input("Digite o comprimento do %iº objeto [Para terminar, digite 0]: " %i))
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

for z in range(qntd_cont):
    print("Contêiner "+str(z+1)+": "+str(C[z]))