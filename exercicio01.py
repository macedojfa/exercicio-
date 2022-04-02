# soma de numeros naturais

def soma(n):
 soma = 0
 for i in range(1,n+1):
    soma = soma + i
 return soma

n= int(input("Digite um número: "))
print(f"A soma dos números de 1 até {n} é :{soma(n)}")