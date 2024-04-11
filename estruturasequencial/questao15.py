15 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R 80,00ouemgalõesde3,6litros,quecustamR  25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações: comprar apenas latas de 18 litros; 
comprar apenas galões de 3,6 litros; misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

metros_quadrados = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros_necessarios = metros_quadrados / 6 * 1.1
latas_18_litros = math.ceil(litros_necessarios / 18)
preco_latas_18_litros = latas_18_litros * 80
galoes_3_6_litros = math.ceil(litros_necessarios / 3.6)
preco_galoes_3_6_litros = galoes_3_6_litros * 25


total_latas_galoes = latas_18_litros + galoes_3_6_litros
litros_restantes = total_latas_galoes * 18 - litros_necessarios
latas_para_comprar = math.ceil(litros_restantes / 18)
galoes_para_comprar = math.ceil((litros_restantes % 18) / 3.6)


preco_misturado = (latas_18_litros * 80) + (galoes_3_6_litros * 25)

print("\nQuantidade de tinta necessária:")
print(f"  - Latas de 18 litros: {latas_18_litros}")
print(f"  - Galões de 3.6 litros: {galoes_3_6_litros}")
print("\nPreços em três situações:")
print(f"  - Comprar apenas latas de 18 litros: R$ {preco_latas_18_litros:.2f}")
print(f"  - Comprar apenas galões de 3.6 litros: R$ {preco_galoes_3_6_litros:.2f}")
print(f"  - Misturar latas e galões: R$ {preco_misturado:.2f}")
