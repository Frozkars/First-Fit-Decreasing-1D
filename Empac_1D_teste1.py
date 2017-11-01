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

C = criar_conjunto(V1,c,n)
qntd_cont=len(C)

for z in range(qntd_cont):
    print("Contêiner "+str(z+1)+": "+str(C[z]))