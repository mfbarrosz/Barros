16 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo em MB: "))

velocidade_internet_mbps = float(input("Digite a velocidade do link de Internet em Mbps: "))
velocidade_mbps_para_mbs = velocidade_internet_mbps / 8

tempo_download_segundos = tamanho_arquivo_mb / velocidade_mbps_para_mbs
tempo_download_minutos = tempo_download_segundos / 60

print(f"O tempo aproximado de download do arquivo será de {tempo_download_minutos:.2f} minutos.")
