11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.
print("2 valores INT, 1 valor FLOAT!")
num1 = int(input("Valor 1:  "))
num2 = int(input("Valor 2: "))
num3 = float(input("Valor 3: "))
produto = (num1 * 2) * (num2 / 2)
soma = (num1 * 3) + (num3 * 3)
cubo = num3 ** 3

print(f"Os valores do produto: {produto} e soma: {soma} e cubo: {cubo}")
