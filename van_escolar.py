
semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado") ##tuple da semana com dias que a van trabalha Seg-Sab
passageiros = [] ##cria uma lista pra armazenar o numero de passageiros
quilometragem = [] ##cria uma lista pra armazenar a quilometragem
mais_de_cinquenta = 0 ##armazena o valor de dias com mais de 50
index=0 ##armazena index para ser utilizado na hora de chamar a tuple semana

for dias in semana: ##para cada dia da semana o programa roda o laço de repetição
    print(semana[index]) ##exibe o dia da semana na tela
    pessoas = int(input("Total de passageiros hoje")) ##pede do usuario valor de pessoas
    kms = int(input("KM total realizado  hoje")) ## pede ao usuario valor de quilometros
    passageiros.append(pessoas) ##adiciona valor à lista
    quilometragem.append(kms) ##adiciona valor à lista
    if pessoas > 50: ##se o valor de pessoas recebido for maior que 50 roda a linha seguinte
        mais_de_cinquenta +=1 ##armazena +1 à variavel
    index+=1 ##adiciona +1 à variável
##A

maior_numero = max(passageiros) ##pega o maior valor da lista
menor_numero = min(passageiros) ##pega o menor valor da lista

##A linha seguinte exibe na tela o dia com maior e menor numero de passageiros, utilizando a função index para descobrir a posição do maior e menor valor na lista passageiros e chama-la na tuple semana
print(f"O dia da semana com o maior numero de passageiros foi: {semana[passageiros.index(maior_numero)]}.\nO dia da semana com o menor numero de passageiros foi: {semana[passageiros.index(menor_numero)]}")

##B

soma_kms = sum(quilometragem) ##Soma toda a lista
media_kms = soma_kms/6 ## Faz a média da semana de trabalho
print(f"A média de KMs rodados nessa semana de trabalho foi : {media_kms:.2f}") ## Mostra na tela o resultado com duas casas de numeros decimais

##C

print(f'O numero de dias que a van transportou mais de 50 passageiros foi: {mais_de_cinquenta} ') ##usa a variavel mais_de_cinquenta pra exibir o numero de dias em que foi transportado mais de 50 passageiros

##D

soma_passageiros = sum(passageiros) ##Soma toda a lista
receita_semanal = soma_passageiros * 14.00 ##multiplica a variavel por 14 e armazena o resultado em outra variavel
despesa_semanal = (soma_kms/11)*6.90 ## divide a variavel depois faz a multiplicação e armazena o resultado em outra variavel
lucro_semanal = receita_semanal - despesa_semanal ##faz o calculo de lucro = receita - despesa

print(f'O lucro dessa semana foi de : {lucro_semanal:.2f}') ## Exibe na tela o lucro da semana com duas casas decimais
