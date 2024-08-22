"""n1 = int(input("Insira um número: "))
i = 0
while i <= n1:
    print(i)
    i+=1"""
"""
print("Deseja calcular dois números?")
resp = input("Digite 'S' para sim, digite 'N' para não: ")

while resp == 'S' or resp == 's':
    print("====================")
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    soma = n1+n2
    print(f"A soma dos dois números é: {soma}")
    print("====================")
    print("Deseja continuar?")
    resp = input("Digite 'S' para sim, digite 'N' para não: ")

    """
def contagemNumero():
    n1 = int(input("Insira um número: "))
    i = 0
    while i <=n1:
        print(i)
        i+=1

def somaInfinita():
    while resp == 'S' or resp == 's':

        print("====================")
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        soma = n1+n2
        print(f"A soma dos dois números é: {soma}")
        print("====================")
        print("Deseja continuar?")
        resp = input("Digite 'S' para sim, digite 'N' para não: ")

def loopInfinito():
    resp = input("Digite um valor: ")
    while resp != "f" and resp != "F":
        print("Dentro do loop.")
        resp = input("Digite um valor: ")

def loopBreak():
    resp = input("Digite um valor: ")
    while resp != "f" and resp != "F":
        print("Dentro do loop.")
        resp = input("Digite um valor: ")
        break

def calculoPar():
    n1 = int(input("Digite um valor: "))
    i = 2
    somaPar = 0
    while i <= n1:
        
        if i % 2 == 0:
            print(i)
            somaPar+=i
        i+=1
    print(f"A soma total de todos os valores é: {somaPar}")

def calculoPotencia():
    n1 = int(input("Insira o primeiro valor: "))
    n2 = int(input("Insira o segundo valor: "))
    if n1 >= 2 and n2 > 1:
        calculo = n1 ** n2
        print(f"O calculo da potência é: {calculo}")

def decimal():
    print("Cálculo de 1/n")
    print("========================")
    n1 = int(input("Insira o valor: "))
    i = 1
    soma = 0

    while i <= n1:
         calculo = 1/i
         soma+=calculo
         i+=1
        
    print(f"A soma total é: {soma:.1f} ")

def contagem():
    n1 = int(input("Insira o valor: "))
    i = 1
    while i <= n1:
        calculo = i ** 2
        print(calculo)
        i+=1
        

contagem()
