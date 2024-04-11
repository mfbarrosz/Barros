#13 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido.
calcule os descontos e o salário líquido, conforme a fórmula abaixo:
Salário Bruto : R −IR(11  - INSS (8%) : R −Sindicato(5  = Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.

  print ("Cálculo do salário")
ganhoPorHora = float(input('Ganho por hora: '))
horasTrabalhadas = float(input('Horas trabalhadas: '))
salario = ganhoPorHora * horasTrabalhadas

print (" ")
print (f"Seu salário é de R${salario}")

Sindicato =  (salario * 0.05)
imposto_de_renda = (salario * 0.11)
INSS = (salario *0.08)
descTotal = salario - (Sindicato + imposto_de_renda + INSS)

print (f"Com desconto IR (11%): R${imposto_de_renda} | Com desconto INSS (8%): R${INSS} | Com desconto Sindicato (5%): R${Sindicato}")
print (f"Salário Liquido (-24%): R$: {descTotal}")
