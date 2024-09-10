#Supondo que o país A tem uma população de 80.000 habitantes com taxa de crescimento de 3% ao ano e que o país B tem 200.000 habitantes com taxa de crescimento de 1,5% ao ano. O código que resolve esse problema escrito na linguagem de programação Python é:
'''
paisA = 80000

paisB = 200000

qtdAnos = 0

while paisB > paisA:

  populacaoPaisA = paisA * 0.03

  populacaoPaisB = paisB * 0.015

  paisA = paisA + populacaoPaisA

  paisB = paisB + populacaoPaisB

  qtdAnos = qtdAnos + 1

print("O país A passará o país B em", qtdAnos, "anos")

populaçãoPaisA = float(input("informe a população da cidade A "))

populaçãoPaisB = float(input("informe a população da cidade B "))
qtdAnos = 0

taxa_anualA=float(input("informe a taxa de crescimento da população da cidade A "))

taxa_anualB=float(input("informe a taxa de crescimento da população da cidade B "))

while populaçãoPaisA < populaçãoPaisB:
	populaçãoPaisA+=round((populaçãoPaisA*taxa_anualA)/0.03)
	populaçãoPaisB+=round((populaçãoPaisB*taxa_anualB)/0.15)
	qtdAnos = qtdAnos + 1

print("levará",qtdAnos,"anos para população da cidade A ser maior que a cidade B")
print("populaçãoPaisB-->",populaçãoPaisB,"habitantes")
print("populaçãoPaisA-->", populaçãoPaisA,"habitantes")'''

#Parte 3 - Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

'''
for i in range(1,51,2):
    print (i)

    '''

#Faça um programa que calcule o mostre a média aritmética de N notas.

'''
Nota1 = float(input( 'Qual foi sua primeira nota? ') )

Nota2 = float(input('E a segunda? '))

Nota3 = float(input( 'E a terceira? '))

Nota4 = float(input('E a quarta? ')) 

Média = (Nota1 + Nota2 + Nota3 + Nota4) / 4

print(f'A nota do aluno ao todo foi {Média}')

'''


#O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
'''
from math import inf

maior = -inf
menor = inf
soma = 0
contador = 0
while True:
    temperatura = float(
        input("Digite a temperatura em Kelvin. Negativa para parar: ")
    )
    if temperatura < 0:
        break

    contador += 1
    soma += temperatura
    if temperatura < menor:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura

print(f"A menor temperatura foi {menor}K")
print(f"A maior temperatura foi {maior}K")
print(f"A média das temperaturas foi {soma / contador:.3f}K")

'''
