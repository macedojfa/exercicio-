# soma de algarismo de um numeros inteiros


def soma_algarismo(numero):
    soma = 0
    while numero > 0:
        resto = numero % 10
        numero = numero // 10
        soma = soma + resto
    return soma

numero = int(input("Digite um numero inteiro: "))
print(f"A soma dos algarismos do numero {numero} é: {soma_algarismo(numero)}")