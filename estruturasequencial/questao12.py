12 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável (peso de peixes) e calcule o excesso. Gravar na variável a quantidade de quilos além do limite e na variável o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.

PesoDoPeixe = float(input("Digite a quantidade de kilos: "))
excesso = PesoDoPeixe - 50

if excesso <= 0:
    print("Não houve excesso de peso.")
    valor_multa = 0
else:
    print(f"Excesso de peso: {excesso:.2f} quilos.")
    valor_multa = excesso * 4

print(f"Valor da multa a ser pago: R$ {valor_multa:.2f}")

